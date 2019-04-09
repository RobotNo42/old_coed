import logging


def test():
    # 1、创建一个logger
    log = logging.getLogger()
    log.setLevel(logging.DEBUG)
    # 2.创建一个handler，用于写入日志文件
    file = logging.FileHandler("test.txt")
    file.setLevel(logging.DEBUG)
    # 再创建一个handler，用于输出到控制台
    stream = logging.StreamHandler()
    stream.setLevel(logging.DEBUG)
    # 3.定义handler的输出格式（formatter）
    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    # 4.给handler添加formatter
    file.setFormatter(formatter)
    stream.setFormatter(formatter)
    # 5.给logger添加handler
    log.addHandler(file)       # logger对象可以添加多个fh和ch对象
    log.addHandler(stream)
    return log


l = test()
l.debug("debug")
l.info("info")
l.warning("warning")
l.error("error")
l.critical("critical")
