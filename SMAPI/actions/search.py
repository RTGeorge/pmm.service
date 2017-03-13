from ..itemTypes import *

def execute(args):
    response = '''
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
  <soap:Body>
    <searchResponse xmlns="http://www.sonos.com/Services/1.1">
      <searchResult>
        <index>0</index>
        <count>3</count>
        <total>3</total>
        <mediaCollection>
          <title></title>
          <itemType>artist</itemType>
          <id>artist:dir:10462312</id>
          <authrequired>0</authrequired>
          <genre>Alternative</genre>
        </mediaCollection>
        <mediaCollection>
          <title></title>
          <itemType>artist</itemType>
          <id>artist:dir:12015032</id>
          <authrequired>0</authrequired>
          <genre>Unknown</genre>
        </mediaCollection>
        <mediaCollection>
          <title></title>
          <itemType>artist</itemType>
          <id>artist:dir:12132174</id>
          <authrequired>0</authrequired>
          <genre>Unknown</genre>
        </mediaCollection>
      </searchResult>
   </searchResponse> 
  </soap:Body> 
</soap:Envelope>
'''
    return response
