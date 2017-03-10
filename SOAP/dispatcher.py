from pysimplesoap.simplexml import SimpleXMLElement

class SOAPDispatcher(object):

    def __init__(self, name, documentation='', action='', location='',
                 namespace=None, prefix=False,
                 soap_uri="http://schemas.xmlsoap.org/soap/envelope/",
                 soap_ns='soap',
                 namespaces={},
                 pretty=False,
                 debug=False,
                 **kwargs):
        """
        :param namespace: Target namespace; xmlns=targetNamespace
        :param prefix: Prefix for target namespace; xmlns:prefix=targetNamespace
        :param namespaces: Specify additional namespaces; example: {'external': 'http://external.mt.moboperator'}
        :param pretty: Prettifies generated xmls
        :param debug: Use to add tracebacks in generated xmls.
        Multiple namespaces
        ===================
        It is possible to support multiple namespaces.
        You need to specify additional namespaces by passing `namespace` parameter.
        >>> dispatcher = SoapDispatcher(
        ...    name = "MTClientWS",
        ...    location = "http://localhost:8008/ws/MTClientWS",
        ...    action = 'http://localhost:8008/ws/MTClientWS', # SOAPAction
        ...    namespace = "http://external.mt.moboperator", prefix="external",
        ...    documentation = 'moboperator MTClientWS',
        ...    namespaces = {
        ...        'external': 'http://external.mt.moboperator',
        ...        'model': 'http://model.common.mt.moboperator'
        ...    },
        ...    ns = True)
        Now the registered method must return node names with namespaces' prefixes.
        >>> def _multi_ns_func(self, serviceMsisdn):
        ...    ret = {
        ...        'external:activateSubscriptionsReturn': [
        ...            {'model:code': '0'},
        ...            {'model:description': 'desc'},
        ...        ]}
        ...    return ret
        Our prefixes will be changed to those used by the client.
        """
        self.methods = {}
        self.name = name
        self.documentation = documentation
        self.action = action  # base SoapAction
        self.location = location
        self.namespace = namespace  # targetNamespace
        self.prefix = prefix
        self.soap_ns = soap_ns
        self.soap_uri = soap_uri
        self.namespaces = namespaces
        self.pretty = pretty
        self.debug = debug

    @staticmethod
    def _extra_namespaces(xml, ns):
        """Extends xml with extra namespaces.
        :param ns: dict with namespaceUrl:prefix pairs
        :param xml: XML node to modify
        """
        if ns:
            _tpl = 'xmlns:%s="%s"'
            _ns_str = " ".join([_tpl % (prefix, uri) for uri, prefix in ns.items() if uri not in xml])
            xml = xml.replace('/>', ' ' + _ns_str + '/>')
        return xml

    def register_function(self, name, fn, returns=None, args=None, doc=None):
        self.methods[name] = fn, returns, args, doc or getattr(fn, "__doc__", "")

    def response_element_name(self, method):
        return '%sResponse' % method

    def dispatch(self, xml, action=None, fault=None):
        """Receive and process SOAP call, returns the xml"""
        # a dict can be sent in fault to expose it to the caller
        # default values:
        prefix = self.prefix
        ret = None
        if fault is None:
            fault = {}
        soap_ns, soap_uri = self.soap_ns, self.soap_uri
        soap_fault_code = 'VersionMismatch'
        name = None

        # namespaces = [('model', 'http://model.common.mt.moboperator'), ('external', 'http://external.mt.moboperator')]
        _ns_reversed = dict(((v, k) for k, v in self.namespaces.items()))  # Switch keys-values
        # _ns_reversed = {'http://external.mt.moboperator': 'external', 'http://model.common.mt.moboperator': 'model'}

        try:
            request = SimpleXMLElement(xml, namespace=self.namespace)

            # detect soap prefix and uri (xmlns attributes of Envelope)
            for k, v in request[:]:
                if v in ("http://schemas.xmlsoap.org/soap/envelope/",
                         "http://www.w3.org/2003/05/soap-env",
                         "http://www.w3.org/2003/05/soap-envelope",):
                    soap_ns = request.attributes()[k].localName
                    soap_uri = request.attributes()[k].value

                # If the value from attributes on Envelope is in additional namespaces
                elif v in self.namespaces.values():
                    _ns = request.attributes()[k].localName
                    _uri = request.attributes()[k].value
                    _ns_reversed[_uri] = _ns  # update with received alias
                    # Now we change 'external' and 'model' to the received forms i.e. 'ext' and 'mod'
                # After that we know how the client has prefixed additional namespaces

            ns = NS_RX.findall(xml)
            for k, v in ns:
                if v in self.namespaces.values():
                    _ns_reversed[v] = k

            soap_fault_code = 'Client'

            # parse request message and get local method
            method = request('Body', ns=soap_uri).children()(0)
            if action:
                # method name = action
                name = action[len(self.action)+1:-1]
                prefix = self.prefix
            if not action or not name:
                # method name = input message name
                name = method.get_local_name()
                prefix = method.get_prefix()

            log.debug('dispatch method: %s', name)
            function, returns_types, args_types, doc = self.methods[name]
            log.debug('returns_types %s', returns_types)

            # de-serialize parameters (if type definitions given)
            if args_types:
                args = method.children().unmarshall(args_types)
            elif args_types is None:
                args = {'request': method}  # send raw request
            else:
                args = {}  # no parameters

            soap_fault_code = 'Server'
            # execute function
            ret = function(**args)
            log.debug('dispathed method returns: %s', ret)

        except SoapFault as e:
            fault.update({
                'faultcode': "%s.%s" % (soap_fault_code, e.faultcode),
                'faultstring': e.faultstring,
                'detail': e.detail
            })

        except Exception:  # This shouldn't be one huge try/except
            import sys
            etype, evalue, etb = sys.exc_info()
            log.error(traceback.format_exc())
            if self.debug:
                detail = u''.join(traceback.format_exception(etype, evalue, etb))
                detail += u'\n\nXML REQUEST\n\n' + xml.decode('UTF-8')
            else:
                detail = None
            fault.update({'faultcode': "%s.%s" % (soap_fault_code, etype.__name__),
                     'faultstring': evalue,
                     'detail': detail})

        # build response message
        if not prefix:
            xml = """<%(soap_ns)s:Envelope xmlns:%(soap_ns)s="%(soap_uri)s"/>"""
        else:
            xml = """<%(soap_ns)s:Envelope xmlns:%(soap_ns)s="%(soap_uri)s"
                       xmlns:%(prefix)s="%(namespace)s"/>"""

        xml %= {    # a %= {} is a shortcut for a = a % {}
            'namespace': self.namespace,
            'prefix': prefix,
            'soap_ns': soap_ns,
            'soap_uri': soap_uri
        }

        # Now we add extra namespaces
        xml = SoapDispatcher._extra_namespaces(xml, _ns_reversed)

        # Change our namespace alias to that given by the client.
        # We put [('model', 'http://model.common.mt.moboperator'), ('external', 'http://external.mt.moboperator')]
        # mix it with {'http://external.mt.moboperator': 'ext', 'http://model.common.mt.moboperator': 'mod'}
        mapping = dict(((k, _ns_reversed[v]) for k, v in self.namespaces.items()))  # Switch keys-values and change value
        # and get {'model': u'mod', 'external': u'ext'}

        response = SimpleXMLElement(xml,
                                    namespace=self.namespace,
                                    namespaces_map=mapping,
                                    prefix=prefix)

        response['xmlns:xsi'] = "http://www.w3.org/2001/XMLSchema-instance"
        response['xmlns:xsd'] = "http://www.w3.org/2001/XMLSchema"

        body = response.add_child("%s:Body" % soap_ns, ns=False)

        if fault:
            # generate a Soap Fault (with the python exception)
            body.marshall("%s:Fault" % soap_ns, fault, ns=False)
        else:
            # return normal value
            res = body.add_child(self.response_element_name(name), ns=self.namespace)
            if not prefix:
                res['xmlns'] = self.namespace  # add target namespace

            # serialize returned values (response) if type definition available
            if returns_types:
                # TODO: full sanity check of type structure (recursive)
                complex_type = isinstance(ret, dict)
                if complex_type:
                    # check if type mapping correlates with return value
                    types_ok = all([k in returns_types for k in ret.keys()])
                    if not types_ok:
                        warnings.warn("Return value doesn't match type structure: "
                                     "%s vs %s" % (str(returns_types), str(ret)))
                if not complex_type or not types_ok:
                    # backward compatibility for scalar and simple types
                    res.marshall(list(returns_types.keys())[0], ret, )
                else:
                    # new style for complex classes
                    for k, v in ret.items():
                        res.marshall(k, v)
            elif returns_types is None:
                # merge xmlelement returned
                res.import_node(ret)
            elif returns_types == {}:
                log.warning('Given returns_types is an empty dict.')

        return response.as_xml(pretty=self.pretty)

    # Introspection functions:

    def list_methods(self):
        """Return a list of aregistered operations"""
        return [(method, doc) for method, (function, returns, args, doc) in self.methods.items()]

    def help(self, method=None):
        """Generate sample request and response messages"""
        (function, returns, args, doc) = self.methods[method]
        xml = """
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
<soap:Body><%(method)s xmlns="%(namespace)s"/></soap:Body>
</soap:Envelope>""" % {'method': method, 'namespace': self.namespace}
        request = SimpleXMLElement(xml, namespace=self.namespace, prefix=self.prefix)
        if args:
            items = args.items()
        elif args is None:
            items = [('value', None)]
        else:
            items = []
        for k, v in items:
            request(method).marshall(k, v, add_comments=True, ns=False)

        xml = """
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
<soap:Body><%(method)sResponse xmlns="%(namespace)s"/></soap:Body>
</soap:Envelope>""" % {'method': method, 'namespace': self.namespace}
        response = SimpleXMLElement(xml, namespace=self.namespace, prefix=self.prefix)
        if returns:
            items = returns.items()
        elif args is None:
            items = [('value', None)]
        else:
            items = []
        for k, v in items:
            response('%sResponse' % method).marshall(k, v, add_comments=True, ns=False)

        return request.as_xml(pretty=True), response.as_xml(pretty=True), doc

    def wsdl(self):
        """Generate Web Service Description v1.1"""
        xml = """<?xml version="1.0"?>
<wsdl:definitions name="%(name)s"
          targetNamespace="%(namespace)s"
          xmlns:tns="%(namespace)s"
          xmlns:soap="http://schemas.xmlsoap.org/wsdl/soap/"
          xmlns:wsdl="http://schemas.xmlsoap.org/wsdl/"
          xmlns:xsd="http://www.w3.org/2001/XMLSchema">
    <wsdl:documentation xmlns:wsdl="http://schemas.xmlsoap.org/wsdl/">%(documentation)s</wsdl:documentation>
    <wsdl:types>
       <xsd:schema targetNamespace="%(namespace)s"
              elementFormDefault="qualified"
              xmlns:xsd="http://www.w3.org/2001/XMLSchema">
       </xsd:schema>
    </wsdl:types>
</wsdl:definitions>
""" % {'namespace': self.namespace, 'name': self.name, 'documentation': self.documentation}
        wsdl = SimpleXMLElement(xml)

        for method, (function, returns, args, doc) in self.methods.items():
            # create elements:

            def parse_element(name, values, array=False, complex=False):
                if not complex:
                    element = wsdl('wsdl:types')('xsd:schema').add_child('xsd:element')
                    complex = element.add_child("xsd:complexType")
                else:
                    complex = wsdl('wsdl:types')('xsd:schema').add_child('xsd:complexType')
                    element = complex
                element['name'] = name
                if values:
                    items = values
                elif values is None:
                    items = [('value', None)]
                else:
                    items = []
                if not array and items:
                    all = complex.add_child("xsd:all")
                elif items:
                    all = complex.add_child("xsd:sequence")
                for k, v in items:
                    e = all.add_child("xsd:element")
                    e['name'] = k
                    if array:
                        e[:] = {'minOccurs': "0", 'maxOccurs': "unbounded"}
                    if v in TYPE_MAP.keys():
                        t = 'xsd:%s' % TYPE_MAP[v]
                    elif v is None:
                        t = 'xsd:anyType'
                    elif isinstance(v, list):
                        n = "ArrayOf%s%s" % (name, k)
                        l = []
                        for d in v:
                            l.extend(d.items())
                        parse_element(n, l, array=True, complex=True)
                        t = "tns:%s" % n
                    elif isinstance(v, dict):
                        n = "%s%s" % (name, k)
                        parse_element(n, v.items(), complex=True)
                        t = "tns:%s" % n
                    else:
                        raise TypeError("unknonw type %s for marshalling" % str(v))
                    e.add_attribute('type', t)

            parse_element("%s" % method, args and args.items())
            parse_element("%sResponse" % method, returns and returns.items())

            # create messages:
            for m, e in ('Input', ''), ('Output', 'Response'):
                message = wsdl.add_child('wsdl:message')
                message['name'] = "%s%s" % (method, m)
                part = message.add_child("wsdl:part")
                part[:] = {'name': 'parameters',
                           'element': 'tns:%s%s' % (method, e)}

        # create ports
        portType = wsdl.add_child('wsdl:portType')
        portType['name'] = "%sPortType" % self.name
        for method, (function, returns, args, doc) in self.methods.items():
            op = portType.add_child('wsdl:operation')
            op['name'] = method
            if doc:
                op.add_child("wsdl:documentation", doc)
            input = op.add_child("wsdl:input")
            input['message'] = "tns:%sInput" % method
            output = op.add_child("wsdl:output")
            output['message'] = "tns:%sOutput" % method

        # create bindings
        binding = wsdl.add_child('wsdl:binding')
        binding['name'] = "%sBinding" % self.name
        binding['type'] = "tns:%sPortType" % self.name
        soapbinding = binding.add_child('soap:binding')
        soapbinding['style'] = "document"
        soapbinding['transport'] = "http://schemas.xmlsoap.org/soap/http"
        for method in self.methods.keys():
            op = binding.add_child('wsdl:operation')
            op['name'] = method
            soapop = op.add_child('soap:operation')
            soapop['soapAction'] = self.action + method
            soapop['style'] = 'document'
            input = op.add_child("wsdl:input")
            ##input.add_attribute('name', "%sInput" % method)
            soapbody = input.add_child("soap:body")
            soapbody["use"] = "literal"
            output = op.add_child("wsdl:output")
            ##output.add_attribute('name', "%sOutput" % method)
            soapbody = output.add_child("soap:body")
            soapbody["use"] = "literal"

        service = wsdl.add_child('wsdl:service')
        service["name"] = "%sService" % self.name
        service.add_child('wsdl:documentation', text=self.documentation)
        port = service.add_child('wsdl:port')
        port["name"] = "%s" % self.name
        port["binding"] = "tns:%sBinding" % self.name
        soapaddress = port.add_child('soap:address')
        soapaddress["location"] = self.location
        return wsdl.as_xml(pretty=True)

