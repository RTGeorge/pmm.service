from pysimplesoap.simplexml import SimpleXMLElement

namespace = "http://www.sonos.com/Services/1.1"

def parseSOAPRequest(xml):
    args = {}

    try:
        request = SimpleXMLElement(xml, namespace)
        for k, v in request[:]:
            if v in ("http://schemas.xmlsoap.org/soap/envelope/",
                     "http://www.w3.org/2003/05/soap-env",
                     "http://www.w3.org/2003/05/soap-envelope",):
                soap_ns = request.attributes()[k].localName
                soap_uri = request.attributes()[k].value

        method = request('Body', ns=soap_uri).children()(0)
        args = method.children().unmarshall({'id':str})
    except:
        print('CRAZY EXCEPTION')
    return args

def generateSOAPResponse(response):
    #SOAPResponse = SimpleXMLElement(response, namespace)
    SOAPResponse = response
    return SOAPResponse
