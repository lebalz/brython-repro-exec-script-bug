import http.server
import socketserver
import os

PORT = 3000
IP = ''

    
class MyRequestHandler(http.server.SimpleHTTPRequestHandler):
    def translate_path(self, path: str) -> str:
        if os.path.isfile(path):
            return path
        return super().translate_path(path)
    def do_GET(self):
        possible_name = f'{self.path.strip("/")}.html'
        static_file = f'{self.path.strip("/")}'
        if self.path == '/':
            self.path = '/index.html'
        elif os.path.isfile(possible_name):
            self.path = possible_name
        elif os.path.isfile(static_file):
            self.path = static_file

        return http.server.SimpleHTTPRequestHandler.do_GET(self)

Handler = MyRequestHandler

with socketserver.TCPServer((IP, PORT), MyRequestHandler) as http_service:
    print(f'Server running at http://{IP or "127.0.0.1"}:{PORT}')
    http_service.serve_forever()