#-*-coding:utf-8-*-
from SocketServer import TCPServer,ThreadingMixIn,StreamRequestHandler

class Server(ThreadingMixIn,TCPServer):pass

class Handler(StreamRequestHandler):
	def handle(self):
		addr=self.request.getpeername()
		print 'Got Connection From ',addr
		self.wfile.write('<html><title>HELL</title><body>Thanks for coming</body></html>')

server=Server(('127.0.0.1',8080),Handler)
server.serve_forever()

