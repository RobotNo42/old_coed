age = 56
i =1
print("你一共有三次机会")
while i <=3:
    print("第" + str(i) + "次机会")
    tell_age = int(input("have a try :"))
    if tell_age >age:
        print("你猜的偏大")

    elif tell_age < age:
        print("你猜的偏小")
    else:
        print("you got it")
        break
    i = i + 1
else:
    print("你没机会了")