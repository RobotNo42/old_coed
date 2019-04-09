import socket
import selectors

sock = socket.socket()
sock.bind(('192.168.1.5', 8022))
sock.listen(5)
sock.setblocking(False)
sel = selectors.DefaultSelector()  # 根据具体平台选择最佳IO多路机制，比如在linux，选择epoll


def read(conn, mask):
    try:
        data = conn.recv(1024)
        print(data.decode('utf-8'))
        data2 = input(">>>>")
        conn.send(data2.encode('utf-8'))
    except Exception:
        sel.unregister(conn)


def accept(so, mask):
    conn, address = so.accept()
    print(conn)
    sel.register(conn, selectors.EVENT_READ, read)


sel.register(sock, selectors.EVENT_READ, accept)  # 注册

while 1:
    print("waiting.......")
    even = sel.select()  # 监听
    for key, mask in even:
        obj = key.fileobj  # print(key.fileobj)    # conn或者sock   对应有变化的对象
        fun = key.data  # print(key.data)       # read或者accept 对应的触发函数
        fun(obj, mask)