def acg(way='file'):
    def happy(func):
        def f1(*arg, **kae):
            if way == 'file':
                with open("D://python/project/python_fullstack/day8/test1.txt",encoding="utf-8") as login_file:
                    x=login_file.read()
                    name_file = eval(x)['name']
                    password_file = eval(x)['password']
                    name = input("input your name:")
                    password = input("input your password")
                    if name == name_file and password == password_file:
                        print("login successful")
                        res = func(*arg, **kae)
                        return res
                    else:
                        print("login error")
            else:
                print("i am not get this way")
        return f1
    return happy


@acg('file')
def login():
    print("welcome to bilibili")
    print("fuck CN")


login()