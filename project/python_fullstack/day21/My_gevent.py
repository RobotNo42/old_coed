import gevent
import time


def w1():
    print('w1 start')
    gevent.sleep(2)
    print('w1 end')


def w2():
    print('w2 start')
    gevent.sleep(5)
    print('w2 end')


start_time = time.time()
gevent.joinall([gevent.spawn(w1), gevent.spawn(w2)])
print(time.time()-start_time)


