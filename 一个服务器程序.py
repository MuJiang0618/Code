#!G:\study\Python
# -*- coding:utf-8 -*-

import socket
server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host=socket.gethostname()
server.bind((host,8088))
server.listen(1)

while True:
    client,addr=server.accept()
    print('got a connection from %s' %str(addr[0]))
    client.send('you are a hero'.encode('utf-8'))
    client.close()