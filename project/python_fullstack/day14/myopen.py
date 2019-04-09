import time


class Open:
    def __init__(self, file, m='r', en='utf-8'):
        self.file = file
        self.m = m
        self.en = en
        self.x = open(file, mode=m, encoding=en)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.x.close()

    def __getattr__(self, item):
        return getattr(self.x, item)

    def write(self, content):
        t = time.strftime("%Y-%m-%d-%X")
        self.x.write('%s       %s' % (t, content))


with Open('b.txt') as f:
    print(f.read())
