"""
Serves files out of its current directory
Dosen't handle POST request
"""

import threading
import webbrowser

from http.server import SimpleHTTPRequestHandler, HTTPServer
from urllib.parse import urlsplit


def double(n=0):
    return str(2 * n)


class CustomHandler(SimpleHTTPRequestHandler):

    def send_page(self, text):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(bytes(text, encoding="utf-8"))

    def do_GET(self):

        if self.path.startswith('/ajax_double'):
            query = urlsplit(self.path).query
            try:
                number = int(query.split("=")[1])
            except ValueError:
                self.send_page("Enter an integer")
                return
            self.send_page(double(number))

        elif self.path == '/quit':
            self.send_page("<h1>Server shutting down.</h1>")
            assassin = threading.Thread(target=server.shutdown)
            print("Server shutting down.")
            assassin.daemon = True
            assassin.start()
        else:
            # serve files, and directory listings by following self.path from
            # current working directory, opening index.html by default if
            # it exists
            SimpleHTTPRequestHandler.do_GET(self)

if __name__ == '__main__':
    port = 8080
    host = "localhost"
    server = HTTPServer((host, port), CustomHandler)
    webbrowser.open("http://{}:{}".format(host, port))
    server.serve_forever()
