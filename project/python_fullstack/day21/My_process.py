import multiprocessing


def work():
    num = 0
    for i in range(400000000):
        num += 1
    print(num)


if __name__ == '__main__':
    process = []
    for i in range(3):
        t = multiprocessing.Process(target=work)
        t.start()
        process.append(t)
    for x in process:
        x.join()

print('fickl')