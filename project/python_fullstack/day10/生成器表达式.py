# l = ['apple%s' % i for i in range(10000)]
# print(l)
#
# g = ('apple%s' % i for i in range(10000))
# for i in g:
#     print(i)
#
# res = []
# with open('test1.txt') as f:
#     for line in f:
#         # print(line)
#         l = line.split(',')
#         # print(l)
#         d = {}
#         d['name'] = l[0]
#         d['price'] = l[1]
#         d['count'] = l[2]
#         res.append(d)
#         print(d)

with open('test1.txt') as f:
    res = (line.split(',') for line in f)
    dic_g = ({'name': i[0], 'price': i[1], 'count': i[2]} for i in res)
    for i in dic_g:
        print(i)