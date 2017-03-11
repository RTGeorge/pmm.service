from urlparse import urlparse
from actions import *

class SMAPIRequest():

    def __init__(self,headers,body):
        self.content = ''
        self.method = 'unknown'
        self.version = 'unknown'
        self.language = headers.getheader('Accept-Language','en')
        self.userAgent = headers.getheader('User-Agent','')

        if headers.getheader('SOAPAction', ''):
            self.dataFormat = 'SOAP'
            actionSpec = urlparse(headers.getheader('SOAPAction'))
            result1 = actionSpec.path.split('/')[-1]
            result2 = actionSpec.fragment
            self.version = result1
            self.method = result2

        elif headers.getheader('JSONAction',''):
            self.dataFormat = 'JSON'

        contentLength = int(headers.getheader('content-length', '0'))
        if contentLength:
            self.content = body.rfile.read(content_len)

    def handle(self):
       exec(self.method + '.execute()')
        
