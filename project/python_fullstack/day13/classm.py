


class mysql:
    def __init__(self, host, port):
        self.host = host
        self.port = port

    @classmethod
    def from_conf(cls):
        print(cls)


print(mysql.from_conf)  # <bound method mysql.from_conf of <class '__main__.mysql'>>

conn = mysql.from_conf()
conn.from_conf()
#
#     def track(self):
#         print('track %s')
#
#
# h = hero()
# h.track()
# hero.track(h)
# print(h.track)
# print(hero.track)
