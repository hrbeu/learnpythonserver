#-*-coding:utf-8-*-
import socket,select
#select模块中的select和poll方法可实现异步I/O
#poll的伸缩性更好，但只能在unix找中使用
s=socket.socket()
host=socket.gethostname()
port=8080
s.bind((host,port))
s.listen(5)

inputs=[s]
while True:

#select使用3个用于输入、输出及异常情况的序列作必选参数
#这些序列是文件描述符
#一个以秒为单位的超时时间作为第四个可选参数
#不设置超时时间则select会阻塞直到其中一个文件描述符已做好准备
#select返回的3个序列（实际是一个长度为3的元组）是对应的3个序列参数的活动子集

	rs,ws,es=select.select(inputs,[],[])
	for r in rs:
		if r is s:
			c,addr=r.accept()
			print 'Got Connection from ',addr
			inputs.append(c)
		else:
			try:
				data=r.recv(1024)
				disconnected=not data
			except socket.error:
				disconnected=True
			if disconnected:
				print r.getpeername(),'disconnected'
				inputs.remove(r)
			else:
				print data
