import time


def happy(func):
    def f1(*arg, **kae):
        start_time = time.time()
        func(*arg, **kae)
        end_time = time.time()
        print('run time is %s' % (end_time-start_time))
    return f1


@happy
def shadow():
    time.sleep(3)
    print("hello_world")


@happy
def auto(name, password):
    print(name, password)


shadow()
auto('wzc', '123456') 
