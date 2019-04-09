def fly(x, y, z=1, *lg, **bo):
    print(x)
    print(y)
    print(z)
    print(lg)
    print(bo)
fly(*(12,16,14,15,18),**{"ni":"fuck","sad":"many"})