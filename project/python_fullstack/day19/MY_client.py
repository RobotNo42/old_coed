import socket
import struct
import json
phone = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
phone.connect(('192.168.1.5', 8020))
while True:
    sd = input("输入:".strip())
    if not sd:
        continue
    phone.send(sd.encode('utf-8'))
    baotou = phone.recv(4)
    baotou_len = struct.unpack('i', baotou)[0]
    head_json = phone.recv(baotou_len).decode('utf-8')
    head_size = json.loads(head_json)
    data_size = head_size['data_size']
    real_content = b''
    real_size = 0
    if real_size < data_size:
        data = phone.recv(1024)
        real_size += len(data)
        real_content += data
    print(real_content.decode('gbk'))
phone.close()
