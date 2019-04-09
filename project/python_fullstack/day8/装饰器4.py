import time

def mom(x='blee'):
    def happy(func):
        def f1(*args, **kwargs):
            """
           fuck u
           """
            print(x)
            start_time = time.time()
            func(*args, **kwargs)
            end_time = time.time()
            print('run time is %s' % (end_time-start_time))
        return f1
    return happy

@mom('red')
def auto(name, password):
    """auto message
       sad sdas as
       dasdasd

    """
    print(name, password)


auto('wzc', '123456')
print(auto.__doc__)