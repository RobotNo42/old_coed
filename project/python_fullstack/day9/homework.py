from urllib.request import urlopen


def get():
    while True:
        url = yield
        res = urlopen(url).read()
        print(res)


g = get()
next(g)
g.send('http://www.buleone.com/cv/wzc.html')