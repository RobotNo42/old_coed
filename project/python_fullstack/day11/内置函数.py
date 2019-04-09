# print(bytes('helloworld', encoding='utf-8'))
# print(dir(sum))
money ={'wzc': 5000, 'lsy': 500, 'hsy': 7000}
# print(money.keys(),money.values())
# print(max(money, key=lambda s: money[s]))
# sor = [2, 4, 6, 1, 34, 3]
# print(sorted(sor))   # 升序
# print(sorted(sor, reverse=True))    # 降序
# print(sorted(money))
# print(sorted(money, key=lambda x: money[x]))


# x = [1, 4, 3, 2, 9, 6]
# l = map(lambda x1: x1**2, x)
# l = map(lambda x1: str(x1) + 'apple', x)
# print(list(l))
#
# from functools import reduce
# print( reduce(lambda x, y: x+y, [1,2,3,4,5]))

fe = [34, 23, 12, 56, 34, 34, 324]
le = filter(lambda x: x > 20, fe)
print(list(le))
li = filter(lambda x1: money[x1] > 1000, money)
print(list(li))
print(round(10.5))
print(round(11.5))