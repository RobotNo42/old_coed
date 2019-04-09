def happy(func):
    def f1(*arg, **kae):
        name = input("input your name:")
        password = input("input your password")
        if name == 'jack' and password == '946971':
            print("login successful")
            res = func(*arg, **kae)
            return res
        else:
            print("login error")
    return f1


@happy
def login():
    print("welcome to bilibili")
    print("fuck CN")


login()