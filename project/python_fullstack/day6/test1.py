
# wzc = open("d://test.txt", mode="w", encoding="utf-8")
# wzc = open("d://test1.txt", mode="w", encoding="utf-8")
# print(wzc.write("fuck u"))
import sys
count = 1
for i in range(100):
    s = "\r%d%% %s" % (i, "#"*i)
    sys.stdout.write(s)
    sys.stdout.flush()
    count += 1
    import time
    time.sleep(0.5) 
