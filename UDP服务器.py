#! G:\study\Python
# -*- coding:utf-8 -*-

import socket
server=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
server.bind(('127.0.0.1',9999))
print('waiting for connection')

while True:
    data,addr=server.recvfrom(1024)
    print(data.decode('utf-8'))
    server.sendto(b'hello',addr)