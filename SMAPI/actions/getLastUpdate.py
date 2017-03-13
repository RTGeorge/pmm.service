from ..itemTypes import *

def execute(args):
    response = '''
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
  <soap:Body>
    <getLastUpdateResponse xmlns="http://www.sonos.com/Services/1.1">
      <getLastUpdateResult>
        <favorites>4321</favorites>
        <catalog>1234</catalog>
        <pollInterval>120</pollInterval>
      </getLastUpdateResult>
    </getLastUpdateResponse>
  </soap:Body>
</soap:Envelope>
'''
    return response
