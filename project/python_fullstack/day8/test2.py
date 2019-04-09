import time


def happy(func):
    def f1(*arg, **kwargs):
        start_time = time.time()
        func(*arg, **kwargs)
        end_time = time.time()
        fina_time = end_time - start_time
        print(fina_time)
    return f1


@happy
def shadow():
    time.sleep(3)
    print("hello_world")


shadow()
