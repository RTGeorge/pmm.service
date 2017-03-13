from ..itemTypes import *

def execute(args):
    response = '''
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
  <soap:Body>
    <getMetadataResponse xmlns="http://www.sonos.com/Services/1.1">
      <getMetadataResult>
        <index>0</index>
        <count>3</count>
        <total>100</total>
        <mediaMetadata>
          <id>track0001</id>
          <title>Kiss Kiss (single)</title>
          <mimeType>audio/x-ms-wma</mimeType>
          <itemType>track</itemType>
          <trackMetadata>
            <albumId>album0001</albumId>
            <duration>253</duration>
            <artistId>artist0001</artistId>
            <artist>Chris Brown</artist>
            <album>Kiss Kiss [featuring T-Pain]</album>
            <albumArtURI>http://example.com/track0001.jpg</albumArtURI>
          </trackMetadata>
        </mediaMetadata>
        <mediaMetadata>
          <id>track0002</id>
          <title>Falling On</title>
          <mimeType>audio/x-ms-wma</mimeType>
          <itemType>track</itemType>
          <trackMetadata>
              <albumId>album0002</albumId>
              <duration>209</duration>
              <artistId>artist:11621038</artistId>
              <genre>Unknown</genre>
              <artist>Finger Eleven</artist>
              <album>Them vs. You vs. Me</album>
              <albumArtURI>http://example.com/track0002.jpg</albumArtURI>
            </trackMetadata>
          </mediaMetadata>
          <mediaMetadata>
            <id>track0003</id>
            <title>My Moon My Man</title>
            <mimeType>audio/x-ms-wma</mimeType>
            <itemType>track</itemType>
              <trackmetadata>
                <albumId>album0003</albumId>
                <duration>184</duration>
                <artistId>artist0003</artistId>
                <artist>Feist</artist>
                <album>The Reminder</album>
                <albumArtURI>http://example.com/track0003.jpg</albumArtURI>
              </trackMetadata>
            </mediaMetadata>
      </getMetadataResult>
    </getMetadataResponse>
  </soap:Body>
</soap:Envelope>
'''
    return response
