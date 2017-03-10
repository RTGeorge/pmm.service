import BaseHTTPServer

class PmmHttpHandler(BaseHTTPServer.BaseHTTPRequestHandler):

    mySuper = BaseHTTPServer.BaseHTTPRequestHandler
    #def __init__(self):
    #    super(pmmHttpHandler, self).__init__()

    def do_GET(self):
        self.mySuper.send_response(self, 200, 'HI')

    def do_Post(self):
