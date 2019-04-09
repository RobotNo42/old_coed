import socket
import selectors

sock = socket.socket()
sock.bind(('192.168.1.5', 8088))
sock.listen(5)
sock.setblocking(False)

sel = selectors.DefaultSelector()  # 根据具体平台选择IO多路机制,win为select,linux为epoll


def reads(con, mask):
    try:
        data = con.recv(1024)
        print(data.decode('utf-8'))
        inp = input(">>>>>回复")
        con.send(inp.encode('utf-8'))
    except Exception:
        sel.unregister(con)


def accepts(sock, mask):
    con, address = sock.accept()
    sel.register(con, selectors.EVENT_READ, reads)


sel.register(sock, selectors.EVENT_READ, accepts)
while True:
    print('please wait........')
    event = sel.select()
    for key, mask in event:
        fun = key.data
        obj = key.fileobj
        fun(obj, mask)