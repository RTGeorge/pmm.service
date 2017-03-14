from ..itemTypes import *

parameters = {
    'id': str,
    'action': str,
    'secondsSinceExplicit': int,
    'deviceSessionToken': str 
}

def execute(args):
    print('THE ARGS')
    print(args)
    if args['id'] == 'track0001':
        response = '''
<s:Envelope xmlns:s="http://schemas.xmlsoap.org/soap/envelope/" xmlns:ns="http://www.sonos.com/Services/1.1">
   <s:Body>
      <ns:getMediaURIResponse>
         <ns:getMediaURIResult>https://s3-us-west-1.amazonaws.com/piday/tim.m4a</ns:getMediaURIResult>
      </ns:getMediaURIResponse>
   </soap:Body>
</soap:Envelope>
'''
    elif args['id'] == 'track0002':
        response = '''
<s:Envelope xmlns:s="http://schemas.xmlsoap.org/soap/envelope/" xmlns:ns="http://www.sonos.com/Services/1.1">
   <s:Body>
      <ns:getMediaURIResponse>
         <ns:getMediaURIResult>https://s3-us-west-1.amazonaws.com/piday/domenic.m4a</ns:getMediaURIResult>
      </ns:getMediaURIResponse>
   </soap:Body>
</soap:Envelope>
'''
    return response
