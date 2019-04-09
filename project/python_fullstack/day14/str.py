class People:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'your name is %s' % self.name


p = People('sb')
print(p)