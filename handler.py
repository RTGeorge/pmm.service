import BaseHTTPServer
from SMAPI.request import SMAPIRequest

class PmmHttpHandler(BaseHTTPServer.BaseHTTPRequestHandler):

    mySuper = BaseHTTPServer.BaseHTTPRequestHandler

    readmeFile = open('README.md','r')
    readme=readmeFile.read()
    readmeFile.close() 

    stringsFile = open('strings.xml','r')
    strings=stringsFile.read()
    stringsFile.close() 
    
    protocol_version='HTTP/1.1'



    def unsupportedHttpMethodResponse(self):
        self.mySuper.send_response(self, 200, 'HTTP METHOD NOT SUPPORTED')

    def createSMAPIRequest(self):
        smapiRequest = SMAPIRequest(self.headers,self.rfile);
        result = smapiRequest.fullfill()
        if smapiRequest.dataFormat == 'SOAP':
            self.send_response(200)
            self.send_header('Content-type', 'text/xml; charset=utf-8')
            self.end_headers()
            self.wfile.write(result)
            self.wfile.close()
        elif smapiRequest.dataFormat == 'JSON':
            self.mySuper.send_response(self, 200, 'JSONY')
        else:
            self.unsupportedHttpMethodResponse()

    def do_CONNECT(self):
        self.unsupportedHttpMethodResponse()
    def do_DELETE(self):
        self.unsupportedHttpMethodResponse()
    def do_GET(self):
        self.mySuper.send_response(self, 200, self.strings)
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
