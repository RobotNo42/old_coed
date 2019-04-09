import json
import os
import struct
import socketserver


class MyFtp(socketserver.BaseRequestHandler):
    coding = 'utf-8'
    server_dir = 'D://test'
    request_size = 5
    max_packet_size = 8000

    def handle(self):
        while True:
            try:
                head_struct = self.request.recv(4)
                if not head_struct:
                    break
                head_size = struct.unpack('i', head_struct)[0]
                head_json = self.request.recv(head_size).decode(self.coding)
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
                file_content = self.request.recv(self.max_packet_size)
                f.write(file_content)
                recv_size += len(file_content)
                print(recv_size)


obj = socketserver.ThreadingTCPServer(('192.168.1.5', 8089), MyFtp)
obj.serve_forever()


