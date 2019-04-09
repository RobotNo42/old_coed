import abc


class AbstractClass(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def walk(self):
        print("caonima")

    @abc.abstractmethod
    def speak(self):
        pass


class People(AbstractClass):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        super().walk()
        print("%s is walk" % self.name)

    def speak(self):
        pass


p = People('汪梓成', 25)
p.speak()
p.walk()