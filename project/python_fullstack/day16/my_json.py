import json


dic = {'hello': 12, 'ko': 47}
f = open("a.txt", "w")
json.dump(dic, f)
f.close()

g = open("a.txt")
print(json.load(g))