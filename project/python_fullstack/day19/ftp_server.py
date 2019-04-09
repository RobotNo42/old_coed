import json
import os
import struct
import socket


class MyFtp:
    coding = 'utf-8'
    address_family = socket.AF_INET
    socket_type = socket.SOCK_STREAM
    server_dir = 'D://test'
    request_size = 5
    max_packet_size = 8000

    def __init__(self, server_address, server_active=True):
        self.server_address = server_address
        self.sock = socket.socket(self.address_family, self.socket_type)
        if server_active:
            try:
                self.server_bind()
                self.server_listen()
            except:
                self.server_close()
                raise

    def server_bind(self):
        self.sock.bind(self.server_address)

    def server_listen(self):
        self.sock.listen(self.request_size)

    def server_close(self):
        self.sock.close()

    def get_requset(self):
        return self.sock.accept()

    def run(self):
        while True:
            self.con,self.client_address = self.get_requset()
            while True:
                try:
                    head_struct = self.con.recv(4)
                    if not head_struct:
                        break
                    head_size = struct.unpack('i', head_struct)[0]
                    head_json = self.con.recv(head_size).decode(self.coding)
                    head_content = json.loads(head_json)
                    cmd = head_content['cmd']
                    if hasattr(self, cmd):
                        fuc = getattr(self, cmd)
                        fuc(head_content)
                except Exception:
                    break

    def put(self, head_content):
        file_path = os.path.normpath(os.path.join(self.server_dir, head_content['file_name']))
        file_size = head_content['file_size']
        recv_size = 0
        with open(file_path, 'wb') as f:
            while recv_size < file_size:
                file_content = self.con.recv(self.max_packet_size)
                f.write(file_content)
                recv_size += len(file_content)
                print(recv_size)

    def download(self, head_content):
        file_path = os.path.normpath(os.path.join(self.server_dir, head_content['file_name']))
        file_exist = os.path.isfile(file_path)
        file_size = os.path.getsize(file_path)
        head_dic = {'file_name': head_content['file_name'], 'file_exist': file_exist, 'file_size': file_size}
        head_json = json.dumps(head_dic)
        head_json_byte = head_json.encode(self.coding)
        head_struct = struct.pack('i', len(head_json_byte))
        # 发送报头的长度
        self.con.send(head_struct)
        # 发送报头
        self.con.send(head_json_byte)
        # 发送内容
        with open(file_path, 'rb') as f:
            for i in f:
                self.con.send(i)


t = MyFtp(('192.168.1.5', 8089))
t.run()





