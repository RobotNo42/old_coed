import socket

BUFSIZE = 1024
ip_port = ('127.0.0.1', 8011)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
res = s.connect_ex(ip_port)

s.send('hello'.encode('utf-8'))
s.send('feng'.encode('utf-8'))
