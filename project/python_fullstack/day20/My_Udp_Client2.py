import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sever_address = ('192.168.1.5', 8089)
while True:
    inp = input(">>>>>>")
    sock.sendto(inp.encode('utf-8'), sever_address)
    data, server = sock.recvfrom(1024)
    print(data.decode('utf-8'))
    print(server)
