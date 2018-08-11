import redis
from socketserver import ForkingMixIn
from http.server import HTTPServer, BaseHTTPRequestHandler
import threading

allowedCalls = ["get", "set"]

def example():
    retString = "http://ip:port/set/foo/10"
    retString = retString + "\n" + "http://ip:port/get/foo"
    return retString

class Handler(BaseHTTPRequestHandler):

    def do_GET(self):
        path = self.path
        if path == "/healthCheck":
            self.send_response(204)
            self.end_headers()
            return
        pathParts = self.path.split('/')[1:]
        if len(pathParts) < 2 or pathParts[0] not in allowedCalls:
            self.send_response(401)
            self.end_headers()
            message = "Allowed calls are:\n{}\n".format(example())
            encodedMessage = message.encode('utf-8')
            self.wfile.write(encodedMessage)
            return
        else:
            self.send_response(200)
            self.end_headers()
            message = "Served from host: {}\n".format(self.connection.getsockname())
            encodedMessage = message.encode('utf-8')
            self.wfile.write(encodedMessage)
            return

class ThreadedHTTPServer(ForkingMixIn, HTTPServer):
    """Handle requests in a separate thread."""

if __name__ == '__main__':
    server = ThreadedHTTPServer(('0.0.0.0', 80), Handler)
    print('Starting server')
    server.request_queue_size = 256
    server.max_children = 128
    server.serve_forever()
