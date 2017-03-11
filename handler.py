import BaseHTTPServer
from SMAPI.request import SMAPIRequest
from SOAP.handler import SOAPHandler

class PmmHttpHandler(BaseHTTPServer.BaseHTTPRequestHandler):

    mySuper = BaseHTTPServer.BaseHTTPRequestHandler

    readmeFile = open('README.md','r')
    readme=readmeFile.read()
    readmeFile.close() 

    def unsupportedHttpMethodResponse(self):
        self.mySuper.send_response(self, 200, 'HTTP METHOD NOT SUPPORTED')

    def createSMAPIRequest(self):
        smapiRequest = SMAPIRequest(self.headers,self.rfile);
        result = smapiRequest.handle()
        if smapiRequest.dataFormat == 'SOAP':
            self.mySuper.send_response(self, 200, result)
        elif smapiRequest.dataFormat == 'JSON':
            self.mySuper.send_response(self, 200, 'JSONY')
        else:
            self.unsupportedHttpMethodResponse()

    def do_CONNECT(self):
        self.unsupportedHttpMethodResponse()
    def do_DELETE(self):
        self.unsupportedHttpMethodResponse()
    def do_GET(self):
        self.mySuper.send_response(self, 200, self.readme)
    def do_HEAD(self):
        self.mySuper.send_response(self, 200)
    def do_OPTIONS(self):
        self.unsupportedHttpMethodResponse()
    def do_POST(self):
        self.createSMAPIRequest()
        #self.mySuper.send_response(self, 200)
    def do_TRACE(self):
        self.unsupportedHttpMethodResponse()
    def do_PUT(self):
        self.unsupportedHttpMethodResponse()
