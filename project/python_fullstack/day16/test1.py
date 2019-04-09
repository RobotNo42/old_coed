import random


def test():
    s = ""
    for i in range(5):
        r1 = random.randint(0, 9)
        r2 = chr(random.randint(65, 90))
        r3 = chr(random.randint(97, 122))
        r4 = random.choice([str(r1), r2, r3])
        s += r4
    return s


print(test())