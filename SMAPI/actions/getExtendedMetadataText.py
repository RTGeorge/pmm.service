from ..itemTypes import *

def execute(args):
    return '''
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
  <soap:Body>
    <getExtendedMetadataTextResponse xmlns="http://www.sonos.com/Services/1.1">
      <getExtendedMetadataTextResult>
        FoxDen Playback Service  
      </getExtendedMetadataTextResult>
    </getExtendedMetadataTextResponse>
  </soap:Body>
</soap:Envelope>
'''
