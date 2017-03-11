from BaseHTTPServer import BaseHTTPRequestHandler
from dispatcher import SOAPDispatcher

class SOAPHandler(BaseHTTPRequestHandler):
    #def __init__(self, request, client_address, parent):
    #    print 'GOBLY1'
    #    parent.dispatcher = SOAPDispatcher(
    #        name="PySimpleSoapSample",
    #        location="http://192.168.11.100:7777/",
    #        action='http://192.168.11.100:7777/',  # SOAPAction
    #        namespace="http://example.com/pysimplesoapsamle/", prefix="ns0",
    #        documentation='Playback My Meeting Service',
    #        trace=True, debug=True,
    #        ns=True)
    #    self.parent = parent
    #    print 'GOBLY2'

    def do_GET(self):
        """User viewable help information and wsdl"""
        args = self.path[1:].split("?")
        if self.path != "/" and args[0] not in self.server.dispatcher.methods.keys():
            self.send_error(404, "Method not found: %s" % args[0])
        else:
            if self.path == "/":
                # return wsdl if no method supplied
                response = self.server.dispatcher.wsdl()
            else:
                # return supplied method help (?request or ?response messages)
                req, res, doc = self.server.dispatcher.help(args[0])
                if len(args) == 1 or args[1] == "request":
                    response = req
                else:
                    response = res
            self.send_response(200)
            self.send_header("Content-type", "text/xml")
            self.end_headers()
            self.wfile.write(response)

    def do_POST(self):
        """SOAP POST gateway"""
        request = self.rfile.read(int(self.headers.get('content-length')))
        # convert xml request to unicode (according to request headers)
        if sys.version < '3':
            encoding = self.headers.getparam("charset")
        else:
            encoding = self.headers.get_param("charset")
        request = request.decode(encoding)
        fault = {}
        # execute the method
        response = self.server.dispatcher.dispatch(request, fault=fault)
        # check if fault dict was completed (faultcode, faultstring, detail)
        if fault:
            self.send_response(500)
        else:
            self.send_response(200)
        self.send_header("Content-type", "text/xml")
        self.end_headers()
        self.wfile.write(response)
