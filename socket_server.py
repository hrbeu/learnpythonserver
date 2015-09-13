#-*-coding:utf-8-*-
from SocketServer import TCPServer,StreamRequestHandler

class  Handler(StreamRequestHandler):
	def handle(self):
                
		addr=self.request.getpeername()
		print 'Got Connection from ' , addr
		self.wfile.write('<html><title>HELL</title><body>Thanks for coming!</body></html>')

server=TCPServer(('127.0.0.1',8080),Handler)
server.serve_forever()









'''
from wsgiref.simple_server import make_server

def application(environ,start_response):
	start_response('200 OK',[('Content-Type','text.html')])
	return '<html><head><title>resign</title></head><body>U JUST QUIT</body></html>'

httpd=make_server('',8000,application)
httpd.serve_forever()
'''



'''
city={
    '北京': '101010100',
    '海淀': '101010200',
    '朝阳': '101010300',
    '顺义': '101010400',
    '怀柔': '101010500',
    '通州': '101010600'
}
for k in city.keys():
    print "%s:%s"%(k.decode('utf-8'),city[k])
'''
