#!G:\study\Python
# -*- coding:utf-8 -*-

import socket

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host=socket.gethostname()
s.connect((host,8088))
msg=s.recv(1024)
print(msg.decode('utf-8'))
s.close()