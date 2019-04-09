import logging


def my_logging():
    log = logging.getLogger()
    log.setLevel(logging.DEBUG)
    handler = logging.FileHandler('test2.txt')
    handler.setLevel(logging.DEBUG)
    stream = logging.StreamHandler()
    stream.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    stream.setFormatter(formatter)
    log.addHandler(stream)
    log.addHandler(handler)
    return log

l = my_logging()
l.debug('debug')
