#! /usr/bin/python
import string
x = raw_input("type something")
if x[0] in string.ascii_lowercase or x in string.ascii_uppercase:
	pass
elif x[0] in string.digits:
	print int(x)+30
else:
	print "some special character"
