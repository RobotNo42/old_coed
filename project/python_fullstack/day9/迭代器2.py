name = {'张三': 24, '李四': 25, '王五': 20}
it = iter(name)
while True:
    try:
        print(next(it))
    except StopIteration:
        break
for i in it:
    print(i)

