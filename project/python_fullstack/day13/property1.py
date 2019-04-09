class People:
    def __init__(self, name, sex):
        self.name = name
        self.sex = sex

    @property
    def sex(self):
        return self.__sex

    @sex.setter
    def sex(self, sex1):
        if not isinstance(sex1, int):
            raise TypeError('必须是数字')
        self.__sex = sex1

    @sex.deleter
    def sex(self):
        del self.__sex


p = People('ezc', 23)

print(p.__dict__)
# print(p.sex)
# p.sex = 15
# print(p.sex)
# del p.sex
# print(p.sex)


