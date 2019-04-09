import sys


class People:
    age = 18

    def walk(self):
        print("fuck u walk")

    # def __setattr__(self, key, value):
    #     print("我是大傻逼")


p = People()
# x = getattr(p, 'wal', '不存在')
# print(x)
# setattr(p, 'age', 18)
# setattr(p, 'height', 100)
# print(p.age)
# print(p.height)


# print(People.__dict__)
# print(p.age)
# print(p.__dict__)
setattr(p, 'age', 20)
print(People.__dict__)
print(p.age)
print(People.age)
print(p.__dict__)
delattr(p, 'age')
print(p.__dict__)


this_modules = sys.modules[__name__]
print(this_modules.People)
print(hasattr(this_modules,'People'))
x = getattr(this_modules, 'People')
w = x()
w.walk()