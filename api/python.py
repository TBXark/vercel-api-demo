from http.server import BaseHTTPRequestHandler
from urlparse import urlparse


class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        name = urlparse.parse_qs(urlparse.urlparse(self.path).query).get('name', "NULL")
        self.wfile.write(("Python: Hello %s!" % name).encode())
        return