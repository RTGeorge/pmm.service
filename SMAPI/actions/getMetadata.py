# -*- coding: utf-8 -*-
from ..itemTypes import *

parameters = {
    'count': int,
    'id': str,
    'index': int,
    'recursive': bool
}

def execute(args):
    response = '''
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
  <soap:Body>
    <getMetadataResponse xmlns="http://www.sonos.com/Services/1.1">
      <getMetadataResult>
        <index>0</index>
        <count>3</count>
        <total>3</total>
        <mediaMetadata>
          <id>track0001</id>
          <itemType>track</itemType>
          <title>📈Meeting1📈</title>
          <genre>Business</genre>
          <mimeType>audio/aac</mimeType>
          <trackMetadata>
            <artistId>user:12345</artistId>
            <artist>G</artist>
            <genre>Business</genre>
            <duration>64</duration>
            <albumArtURI>https://s3-us-west-1.amazonaws.com/piday/meeting1.jpg</albumArtURI>
            <canPlay>true</canPlay>
            <canSkip>true</canSkip>
          </trackMetadata>
        </mediaMetadata>
        <mediaMetadata>
          <id>track0002</id>
          <itemType>track</itemType>
          <title>📝Meeting2📝</title>
          <genre>Business</genre>
          <mimeType>audio/aac</mimeType>
          <trackMetadata>
            <artistId>user:12345</artistId>
            <artist>Domenic</artist>
            <genre>Business</genre>
            <duration>59</duration>
            <albumArtURI>https://s3-us-west-1.amazonaws.com/piday/meeting2.jpg</albumArtURI>
            <canPlay>true</canPlay>
            <canSkip>true</canSkip>
          </trackMetadata>
        </mediaMetadata>
        <mediaMetadata>
          <id>track0003</id>
          <itemType>track</itemType>
          <title>😎Meeting3😎</title>
          <genre>Business</genre>
          <mimeType>audio/aac</mimeType>
          <trackMetadata>
            <artistId>user:12345</artistId>
            <artist>Jeff</artist>
            <genre>Business</genre>
            <duration>57</duration>
            <albumArtURI>https://s3-us-west-1.amazonaws.com/piday/meeting3.jpg</albumArtURI>
            <canPlay>true</canPlay>
            <canSkip>true</canSkip>
          </trackMetadata>
        </mediaMetadata>
      </getMetadataResult>
    </getMetadataResponse>
  </soap:Body>
</soap:Envelope>
'''
    return response
