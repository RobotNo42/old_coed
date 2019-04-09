import json
import struct
import os
import socket


class MyClient:
    coding = 'utf-8'
    address_family = socket.AF_INET
    socket_type = socket.SOCK_STREAM
    client_dir = 'D://client'
    max_packet_size = 8000

    def __init__(self, client_address, client_active=True):
        self.client_address = client_address
        self.sock = socket.socket(self.address_family, self.socket_type)
        if client_active:
            try:
                self.client_connect()
            except:
                self.client_close()
                raise

    def client_connect(self):
        self.sock.connect(self.client_address)

    def client_close(self):
        self.sock.close()

    def run(self):
        print('请输入命令以及要上传的文件的路径')
        while True:
            inp = input(">>: ").strip()
            if not inp:
                continue
            inp_split = inp.split()
            cmd = inp_split[0]
            if hasattr(self, cmd):
                fu = getattr(self, cmd)
                fu(inp_split)

    def put(self, args):
        cmd = args[0]
        filename = args[1]
        if not os.path.isfile(filename):
            print('file:%s is not exists' % filename)
            return
        else:
            filesize = os.path.getsize(filename)
        head_dic = {'cmd': cmd, 'file_name': os.path.basename(filename), 'file_size': filesize}
        head_json = json.dumps(head_dic)
        head_json_bytes = head_json.encode(self.coding)
        head_struct = struct.pack('i', len(head_json_bytes))
        # 发送报头的长度
        self.sock.send(head_struct)
        # 发送真正的报头
        self.sock.send(head_json_bytes)
        # 发送内容
        send_size = 0
        with open(filename, 'rb') as f:
                for i in f:
                    self.sock.send(i)
                    send_size += len(i)
                    print(send_size)
                else:
                    print('upload successful')


c = MyClient(('192.168.1.5', 8089))
c.run()
