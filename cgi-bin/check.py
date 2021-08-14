#!/usr/bin/python3

import cgi
import cgitb
import time
import subprocess

cgitb.enable()

webdata=cgi.FieldStorage()
print("Content-Type: text/html")
print("")


login = {'user':'lnb','password':'ajaj'}
username=webdata.getvalue('u')
pass1 = webdata.getvalue('p')

if username == login ['user'] and pass1 == login['password']:
    print("Logged in Successfuly")
    print("Please Wait")
    print('<meta http-equiv="refresh" content="1;url=http://3.109.167.61/list.html" />')

else:
    print("Invalid Credentials, Try again.")
    print("Redirecting you to Home Page")
    time.sleep(1)
    print('<meta http-equiv="refresh" content="3;url=http://3.109.167.61/" />')

