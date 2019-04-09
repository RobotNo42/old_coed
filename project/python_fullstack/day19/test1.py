import socket
import subprocess
phone = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
phone.bind(('192.168.1.5', 8016))
phone.listen(5)
print('start....')
while True:
    conf,message = phone.accept()
    print(conf)
    print(message)
    while True:
        try:
            data = conf.recv(1024)
            print(data)
            data_tr = data.decode('utf-8')

        except Exception:
            break
    conf.close()
phone.close()
