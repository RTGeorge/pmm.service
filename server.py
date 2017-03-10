import BaseHTTPServer
import conf
from SOAP.handler import SOAPHandler
from SOAP.dispatcher import SOAPDispatcher

soapDispatcher = SOAPDispatcher(
        name="Playback My Meeting",
        location="http://192.168.11.100:7777/",
        action='http://192.168.11.100:7777/',  # SOAPAction
        namespace="http://example.com/pysimplesoapsamle/", prefix="ns0",
        documentation='Playback My Meeting Service',
        trace=True, debug=True,
        ns=True)

pmmd = BaseHTTPServer.HTTPServer((conf.interface, conf.port), SOAPHandler)
pmmd.dispatcher = soapDispatcher
pmmd.serve_forever()
