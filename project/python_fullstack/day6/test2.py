wzc = open("d://test.txt", mode="w+", encoding="utf-8")
wzc.write("happy")
wzc.write("me")
wzc.flush()
print(wzc.read())