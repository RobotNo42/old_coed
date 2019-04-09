messi = []
for i in range(100):
    if i > 50:
        messi.append("apple%s" % i)


l = ["apple%s" % i for i in range(100) if i > 50]  # 'apple%s' %i 这句话在列表中，所以不用append命令写入列表中


x1 = [1, 2, 3, 4]
s = "month"
le = [(num, s1) for num in x1 if num > 2 for s1 in s]
print(le)

x1 = [1, 2, 3, 4]
s = 'month'
x2 = []
for num in x1:
    for s1 in s:
        if num > 2:
            t = (num, s1)
            x2.append(t)
print(x2)