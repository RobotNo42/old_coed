import threading
import logging
import time

logging.basicConfig(level=logging.DEBUG, format='%(threadName)s ------%(message)s')


def work(event):
    while not event.is_set():
        logging.debug('please wait for redis----------%s' % time.ctime())
        event.wait(2)
    logging.debug('redis ready, and connect to redis server and do some work [%s]', time.ctime())
    # time.sleep(1)


def main():
    read_redis = threading.Event()
    t1 = threading.Thread(target=work, args=(read_redis,), name='t1')
    t1.start()
    t2 = threading.Thread(target=work, args=(read_redis,), name='t2')
    t2.start()
    logging.debug("please wait thr main redis start")
    time.sleep(16)
    read_redis.set()


if __name__ == '__main__':
    main()