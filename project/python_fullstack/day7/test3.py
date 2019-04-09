def f3():
    x = 1
    def f4():
        print(x)
    return f4

x = 1000
f4 = f3()
f4()