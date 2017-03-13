from ..itemTypes import *

def execute(args):
    response = '''
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
  <soap:Body>
    <getExtendedMetadataResponse xmlns="http://www.sonos.com/Services/1.1">
      <getExtendedMetadataResult>
        <mediaMetadata>
          <id>{ID}</id>
          <itemType>track</itemType>
          <title>Example Track</title>
          <mimeType>audio/mp3</mimeType>
          <trackMetadata>
            <artistId>A:123456</artistId>
            <artist>Dethklok</artist>
            <albumid>M:123456</albumid>
            <album>Dethalbum II</album>
            <duration>343</duration>
            <albumArtURI>http://example.com/images/aa/1.jpg</albumArtURI>
            <canSkip>true</canSkip>
            <canAddToFavorites>true</canAddToFavorites>
          </trackMetadata>
        </mediaMetadata>
      </getExtendedMetadataResult>
    </getExtendedMetadataResponse>
  </soap:Body>
</soap:Envelope>
'''
    return response.format(ID=args['id'])
