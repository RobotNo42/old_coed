import socket
phone = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
phone.connect(('192.168.1.5', 8014))
while True:
    sd = input("输入:".strip())
    if not sd:
        continue
    phone.send(sd.encode('utf-8'))
    message = phone.recv(1024)
    print(message)
phone.close()
