import calendar
import time
from ..itemTypes import *

parameters = {}

def execute(args):
    timestamp = calendar.timegm(time.gmtime())
    response = '''
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
  <soap:Body>
    <getLastUpdateResponse xmlns="http://www.sonos.com/Services/1.1">
      <getLastUpdateResult>
        <favorites>0</favorites>
        <catalog>{version}</catalog>
        <pollInterval>120</pollInterval>
      </getLastUpdateResult>
    </getLastUpdateResponse>
  </soap:Body>
</soap:Envelope>
'''
    return response.format(version=timestamp)
