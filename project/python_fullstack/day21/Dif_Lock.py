import time
import threading


def sup_num():
    global Num
    print('ok')
    lock.acquire()
    ji = Num
    time.sleep(0.0001)
    Num = ji - 1
    lock.release()


Num = 100
lock = threading.Lock()
thread_list = []

for i in range(100):
    t = threading.Thread(target=sup_num)
    t.start()
    thread_list.append(t)

for t in thread_list:
    t.join()

print('Result: ', Num)
