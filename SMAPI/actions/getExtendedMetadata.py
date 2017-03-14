# -*- coding: utf-8 -*-
from ..itemTypes import *

parameters = {
    'id': str
}

def execute(args):
    response = '''
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
  <soap:Body>
    <getExtendedMetadataResponse xmlns="http://www.sonos.com/Services/1.1">
      <getExtendedMetadataResult>
        <mediaMetadata>
          <id>{ID}</id>
          <itemType>track</itemType>
          <title>📈 Super Important Meeting #1📈</title>
          <mimeType>audio/aac</mimeType>
        </mediaMetadata>
      </getExtendedMetadataResult>
    </getExtendedMetadataResponse>
  </soap:Body>
</soap:Envelope>
'''
    return response.format(ID=args['id'])
