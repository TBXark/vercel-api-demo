from http.server import BaseHTTPRequestHandler

class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        data = [x for i,x in enumerate(self.path.split("?")[1].split("&")) if x.split("=")[0] == "name"]
        name = "NULL"
        if len(data) > 0:
            name = data[0].split("=")[1]
        self.wfile.write(("Python: Hello %s!" % name).encode())
        return