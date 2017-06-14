#!usr/bin/python
import socket

x = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sip = "192.168.42.14"
sport = 8888

while True :
	msg=raw_input("enter your message")
	x.sendto(msg,(sip,sport))
	rec=x.recvfrom(100)
	print "message from server"
	print rec[0] 
