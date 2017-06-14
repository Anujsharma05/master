#!usr/bin/python2
import socket 

x=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

user=raw_input("enter your username: ")
pasw=raw_input("enter your password: ")

ip="192.168.42.174"
port=5555
x.sendto(user,(ip,port))
x.sendto(pasw,(ip,port))

print  x.recvfrom(100)
while True:	
	command=raw_input("enter the command: ")
	x.sendto(command,(ip,port))
	result = x.recvfrom(100)
	print result[0]
