def happy(cls):
    instances = {}

    def f(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return f


@happy
class Add(object):
    pass


