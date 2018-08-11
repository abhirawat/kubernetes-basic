import redis
from socketserver import ForkingMixIn
from http.server import HTTPServer, BaseHTTPRequestHandler
import threading
import sys

allowedCalls = ["get", "set"]
if len(sys.argv) == 3:
    redis_ip = sys.argv[1]
    redis_port = sys.argv[2]
else:
    print("Usage: app.py redis_ip redis_port")
    sys.exit(1)

redisConn = redis.StrictRedis(host=redis_ip, port=redis_port, db=0)

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
        if pathParts[0] not in allowedCalls or (pathParts[0] == "get" and len(pathParts) < 2) or (pathParts[0] == "set" and len(pathParts) < 3):
            self.send_response(400)
            self.end_headers()
            message = "Allowed calls are:\n{}\n".format(example())
            encodedMessage = message.encode('utf-8')
            self.wfile.write(encodedMessage)
            return
        else:
            message = "Served from host: {}\n".format(self.connection.getsockname())
            command = pathParts[0]
            key = pathParts[1]
            if command == "set":
                value = pathParts[2]
                redisConn.set(key,value)
                message = message + "Done" + "\n"
            if command == "get":
                value = redisConn.get(key)
                if value == None:
                    value = "None"
                message = message + value.decode('utf-8') + "\n"
            self.send_response(200)
            self.end_headers()
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
