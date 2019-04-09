
def happy(fuc):
    def f1(*arg, **kae):
        res = fuc(*arg, **kae)
        next(res)
        return res
    return f1


@happy
def menu(x):
    print("welcome %s to shaxian restaurant" % x)
    men_list = []
    while True:
        print(men_list)
        food = yield men_list
        print("%s start to eat %s" % (x, food))
        men_list.append(food)


g = menu('汪梓成')
g.send('包子')        # 将'包子'传给yield ，然后赋值给了food，然后从上次暂停的位置接着执行代码，直到又到下一个yield
g.send('饺子')
g.send('牛肉面')