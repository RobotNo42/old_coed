import socket

sock = socket.socket()
sock.connect(('192.168.1.5', 8020))
while True:
    inp = input('>>>>>>输入')
    sock.send(inp.encode('utf-8'))
    re = sock.recv(1024)
    print(re.decode('utf-8'))