class People:
    def __init__(self, name, age, weight, height):
        self.name = name
        self.age =age
        self.weight = weight
        self.height = height

    @property
    def dmi(self):
        d = self.weight / (self.height ** 2)
        return round(d, 2)


g = People('wzc', 20, 75, 1.7)
print(g.dmi)