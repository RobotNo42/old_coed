from threading import Thread
import time


class MyThread(Thread):

    def __init__(self, num):
        super().__init__()
        self.num = num

    def run(self):
        print("running on number:%s" % self.num)
        time.sleep(3)


t1 = MyThread(56)
t2 = MyThread(78)

t1.start()
t2.start()
print("ending")