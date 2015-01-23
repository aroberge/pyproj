"""
Serves files out of its current directory with ajax test
"""

import threading
import webbrowser

from http.server import SimpleHTTPRequestHandler, HTTPServer
from urllib.parse import urlsplit


def double(n=0):
    '''simple test function'''
    return str(2 * n)


class CustomHandler(SimpleHTTPRequestHandler):

    def send_page(self, text):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(bytes(text, encoding="utf-8"))

    def do_GET(self):  # noqa

        if self.path.startswith('/ajax_double'):
            query = urlsplit(self.path).query
            try:
                number = int(query.split("=")[1])
            except ValueError:
                self.send_page("Enter an integer")
                return
            self.send_page(double(number))

        elif self.path == '/quit':
            self.send_page("<h3>Server shutting down.</h3>")
            # ... from Python's REPL
            # >>> help(socketserver.BaseServer.shutdown)
            # Help on function shutdown in module socketserver:

            # shutdown(self)
            #     Stops the serve_forever loop.

            #     Blocks until the loop has finished. This must be called while
            #     serve_forever() is running in another thread, or it will
            #     deadlock.
            shut_it_down = threading.Thread(target=server.shutdown, daemon=True)
            print("Server shutting down.")
            shut_it_down.start()
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
