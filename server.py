#!usr/bin/python
import socket

x=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
x.bind(("",8888))

while True :
	s=x.recvfrom(100)
	print "message from client"
	print s
	rply=raw_input("send reply : ")
	x.sendto(rply,s[1])
