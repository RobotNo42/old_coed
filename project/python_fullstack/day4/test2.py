linux = {"alex", "jack", "rain", "lizhi", "sb", "lizhi"}
python = {"sb", "alex", "mack", "rachel"}

print(linux.intersection(python))  # 交集
print(linux & python)            # 交集
print(linux.difference(python))  # 差集 linux中有而python中没有
print(linux - python)            # 差集 linux中有而python中没有
print(linux.union(python))       # 并集
print(linux | python)            # 并集
print(linux.symmetric_difference(python))  # 对称 互相不在的都打印
print(linux ^ python)                      # 对称 互相不在的都打印
