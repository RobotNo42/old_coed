from threading import Thread
import time


class MyThread(Thread):
    def __init__(self, name,my_time):
        Thread.__init__(self)
        self.name = name
        self.my_time = my_time

    def run(self):
        print('it is %s              %s' % (self.name, time.ctime()))
        time.sleep(self.my_time)
        print('%s end                %s ' % (self.name, time.ctime()))


t1 = MyThread('WZC', 3)
t2 = MyThread('LSY', 5)
t1.setDaemon(True)
t1.start()
t2.start()
print('fuck')
