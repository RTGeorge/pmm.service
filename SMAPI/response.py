from urlparse import urlparse
from actions import *
from SOAP.parser import parseSOAPRequest

class SMAPIRequest():

    def __init__(self,headers,body):
        # Field 1: error stat - 0 success, content or result
        self.result = {1, 'GOBLY'}
        self.method = 'unknown'
        self.version = 'unknown'
        self.language = headers.getheader('Accept-Language','en')
        self.userAgent = headers.getheader('User-Agent','')
        self.content = ''
        self.args = {}

        encoding = headers.getheader('charset', '')
        contentLength = int(headers.getheader('content-length', 0))
        if contentLength:
            self.content = body.read(contentLength)
        if encoding:
            self.content = self.content.decode(encoding)

        if headers.getheader('SOAPAction', ''):
            self.dataFormat = 'SOAP'
            actionSpec = urlparse(headers.getheader('SOAPAction'))
            self.version = actionSpec.path.split('/')[-1]
            self.method = actionSpec.fragment
            self.args = parseSOAPRequest(self.content)
        elif headers.getheader('JSONAction',''):
            self.dataFormat = 'JSON'

    def fullfill(self):
       return globals()[self.method].execute(self.args)
