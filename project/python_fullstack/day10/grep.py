import os


def search():
    while True:
        dir_name = yield
        g = os.walk(dir_name)
        for i in g:
            for x in i[-1]:
                print("%s/%s" % (i[0], x))


g = search()
next(g)
g.send('d:/python')