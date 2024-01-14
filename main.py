#!/usr/bin/env python3

import webbrowser
from http.server import SimpleHTTPRequestHandler
from socketserver import TCPServer

class MyHandler(SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Location', '/index.html')
        super().end_headers()

def run_server():
    port = 8000
    server_address = ('', port)

    httpd = TCPServer(server_address, MyHandler)

    print(f"Serving on http://localhost:{port}")
    webbrowser.open(f'http://localhost:{port}/index.html')
    
    httpd.serve_forever()

if __name__ == '__main__':
    run_server()

