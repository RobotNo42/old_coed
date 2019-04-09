def pr(x):
    print("start games")
    while x > 0:
        yield x
        x -= 1
    print("game over")


game = pr(5)

for i in game:
    print(i)
