class Dog():
    country = 'china'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def track(self, somebady):
        print("%s track %s" % (self.name, somebady))


g = Dog('sb', 20)
g.country = 'japan'
g1 = Dog('sd', 12)
print(g.track('sddd'))
