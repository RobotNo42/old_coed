from greenlet import greenlet

def w1():
    print(56)
    g2.switch()
    print(61)
def w2():
    print(11)
    g1.switch()
    print(66)


g1 = greenlet(w1)
g2 = greenlet(w2)
g1.switch()