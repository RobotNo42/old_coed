import time


class FileHandler:
    def __init__(self, filename, mode='r', encoding="utf-8"):
        self.file = open(filename, mode, encoding=encoding)
        # self.file获取到一个文件句柄

    def write(self, line):
        t = time.strftime("%Y-%m-%d %X")
        self.file.write("%s %s" % (t, line))

    def __getattr__(self, item):
        return getattr(self.file, item)
        # 当对象调用FileHandler类不存在的方法时，会返回open()函数的item字符串对应的方法；


f1 = FileHandler("b.txt", "r+")
f1.write("你好吗\n")
f1.seek(0)
print(f1.tell())