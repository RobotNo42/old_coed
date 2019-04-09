import socketserver


class MyUdpServer(socketserver.BaseRequestHandler):
    def handle(self):
        print(self.request[0])
        print(self.request[1])
        self.request[1].sendto('草拟吗'.encode('utf-8'), self.client_address)


if __name__ == '__main__':
    obj = socketserver.ThreadingUDPServer(('192.168.1.5', 8089), MyUdpServer)
    obj.serve_forever()
