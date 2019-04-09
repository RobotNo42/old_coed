class My_type(type):
    def __init__(self, class_name, class_base, class_dict):
        for key in class_dict:
            if not callable(class_dict[key]):
                continue
            if not class_dict[key].__doc__:
                raise TypeError('给我写注释啊')


class Foo(metaclass=My_type):
    """ just a test """
    x = 1

    def ko(self):
        """ just a function """
        print("f")
print(Foo.__doc__)
print(Foo.ko.__doc__)


