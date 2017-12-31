#! G:\study\Python
# -*- coding:utf-8 -*-

import socket

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.sendto(b'hello',('127.0.0.1',9999))
msg,addr=s.recvfrom(1024)
print(msg.decode('utf-8'))
