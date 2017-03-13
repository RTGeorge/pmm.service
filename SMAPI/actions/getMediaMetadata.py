from ..itemTypes import *

def execute(args):
    response = '''
<s:Envelope xmlns:s="http://schemas.xmlsoap.org/soap/envelope/" xmlns:ns="http://www.sonos.com/Services/1.1">
   <s:Body>
      <ns:getMediaMetadataResponse>
         <ns:getMediaMetadataResult>
            <ns:id>track61</ns:id>
            <ns:itemType>track</ns:itemType>
            <ns:title>Giorgio Moroder - Giorgios Theme</ns:title>
            <ns:genre>Electronic</ns:genre>
            <ns:mimeType>audio/mp3</ns:mimeType>
            <ns:trackMetadata>
               <ns:artistId>user:12345</ns:artistId>
               <ns:artist>Williams Street Records</ns:artist>
               <ns:genre>Electronic</ns:genre>
               <ns:duration>459</ns:duration>
               <ns:albumArtURI>https://example.com/image123-large.jpg?abc</ns:albumArtURI>
               <ns:canPlay>true</ns:canPlay>
               <ns:canSkip>true</ns:canSkip>
               <ns:canAddToFavorites>true</ns:canAddToFavorites>
            </ns:trackMetadata>
            <ns:dynamic>
               <ns:property>
                  <ns:name>LIKED</ns:name>
                  <ns:value>1</ns:value>
               </ns:property>
            </ns:dynamic>
         </ns:getMediaMetadataResult>
      </ns:getMediaMetadataResponse>
   </s:Body>
</s:Envelope>
'''
    return response
