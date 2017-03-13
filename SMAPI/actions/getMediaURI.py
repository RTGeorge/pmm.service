from ..itemTypes import *

def execute(args):
    response = '''
<soap:Envelope xmlns:s="http://schemas.xmlsoap.org/soap/envelope/" xmlns:ns="http://www.sonos.com/Services/1.1">
   <soap:Body>
      <ns:getMediaURIResponse>
         <ns:getMediaURIResult>http://acme.example.com/music/track001.mp3</ns:getMediaURIResult>
      </ns:getMediaURIResponse>
   </soap:Body>
</soap:Envelope>
'''
    return response
