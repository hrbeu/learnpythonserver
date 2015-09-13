#-*-coding:utf-8-*-
#windows不支持fork
import SocketServer.TCPServer,ForkingMixIn,StreamRequestHandler

class Server(ForkingMixIn,TCPServer):
	pass

class Handler(StreamRequestHandler):
	def handler(self):
		addr=self.request.getpeername()
		print 'Got Connection from ' addr
		self.wfile.write('<html><title>HELL</title><body>Thanks for coming.</body></html>')

server=Server(('127.0.0.1',8080),Handler)
server.serve_forever()
