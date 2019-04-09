class My_range:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.start == self.end:
            raise StopIteration
        n = self.start
        self.start += 1
        return n


s = My_range(1, 20)
for i in s:
    print(i)