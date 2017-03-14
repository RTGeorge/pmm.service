# -*- coding: utf-8 -*-
from ..itemTypes import *

parameters = {
    'id': str
}

def execute(args):
    print('THE ARGS')
    print(args)
    if args['id'] == 'track0001':
        response = '''
<s:Envelope xmlns:s="http://schemas.xmlsoap.org/soap/envelope/" xmlns:ns="http://www.sonos.com/Services/1.1">
   <s:Body>
      <ns:getMediaMetadataResponse>
         <ns:getMediaMetadataResult>
           <ns:id>track0001</ns:id>
           <ns:itemType>track</ns:itemType>
           <ns:title>📈Meeting1📈</ns:title>
           <ns:genre>Business</ns:genre>
           <ns:mimeType>audio/aac</ns:mimeType>
           <ns:trackMetadata>
             <ns:artistId>user:12345</ns:artistId>
             <ns:artist>G</ns:artist>
             <ns:genre>Business</ns:genre>
             <ns:duration>64</ns:duration>
               <ns:albumArtURI>https://s3-us-west-1.amazonaws.com/piday/meeting1.jpg</ns:albumArtURI>
               <ns:canPlay>true</ns:canPlay>
               <ns:canSkip>true</ns:canSkip>
            </ns:trackMetadata>
         </ns:getMediaMetadataResult>
      </ns:getMediaMetadataResponse>
   </s:Body>
</s:Envelope>
'''
    elif args['id'] == 'track0002':
        response = '''
<s:Envelope xmlns:s="http://schemas.xmlsoap.org/soap/envelope/" xmlns:ns="http://www.sonos.com/Services/1.1">
   <s:Body>
      <ns:getMediaMetadataResponse>
         <ns:getMediaMetadataResult>
           <ns:id>track0002</ns:id>
           <ns:itemType>track</ns:itemType>
           <ns:title>📝Meeting2📝</ns:title>
           <ns:genre>Business</ns:genre>
           <ns:mimeType>audio/aac</ns:mimeType>
           <ns:trackMetadata>
             <ns:artistId>user:12345</ns:artistId>
             <ns:artist>Domenic</ns:artist>
             <ns:genre>Business</ns:genre>
             <ns:duration>59</ns:duration>
               <ns:albumArtURI>https://s3-us-west-1.amazonaws.com/piday/meeting2.jpg</ns:albumArtURI>
               <ns:canPlay>true</ns:canPlay>
               <ns:canSkip>true</ns:canSkip>
            </ns:trackMetadata>
         </ns:getMediaMetadataResult>
      </ns:getMediaMetadataResponse>
   </s:Body>
</s:Envelope>
'''
    return response
