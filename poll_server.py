#-*-coding:utf-8-*-
import socket,select
host='127.0.0.1'
port=8080
s=socket.socket()
s.bind((host,port))

fdmap={s.fileno():s}

s.listen(5)
#poll在windows中不可用
p=select.poll()
#poll对象的register函数用于注册一个文件描述符,unregister函数移除注册的对象
p.register(s)

while True:
#poll返回如[(fd1,event1),(fd2,event2),(fd3,event3),(fd4,event4),...]
	events=p.poll()
	for fd,event in events:
		if fd==s.fileno():
			c,addr=s.accept()
			print 'Got Connection from ',addr
			p.register(c)
			fdmap[c.fileno()]=c
		elif event & select.POLLIN:
			data=fdmap[fd].recv(1024)
			if not data:
				print fdmap[fd].getpeername,'disconnected'
				p.unregister(fd)
				del fdmap[fd]
			print data
