items = ["Macbook", "剃须刀", "cherry", "ps4pro", "switch", "xboxone"]
price = [10000, 300, 1600, 2500, 3000, 2000]
buy_items = []
buy_price = []
total_money = int(input("输入你的工资"))
first_money = total_money
while True:
    print("你能买的东西如下")
    for i in range(len(items)):
        print(i+1, "\t",  items[i], "\t", (price[i]))
    num = input("输入你想要购买的商品编号,退出请输入q :").strip()
    if num.isdigit():
        if int(num) < 1 or int(num) > 6:
            print("请输入正确的编号")
        else:
            if total_money < price[int(num)-1]:
                print("你卡上钱不够，物品价格是",price[int(num)-1], "你还差", (price[int(num)-1]-total_money))
            else:
                total_money = total_money - price[int(num)-1]
                buy_items.append(items[int(num)-1])
                buy_price.append(price[int(num)-1])
                print("购买成功，你的余额还剩", total_money)
    elif num == "q":
        if total_money == first_money:
            print("穷逼啥也不买，滚吧")
            break
        else:
            print("你买了以下东西:")
            for x in range(len(buy_price)):
                print(x+1, "\t", buy_items[x], "\t", buy_price[x])
            print("余额：", total_money)
            print("再见！")
            break
    else:
        print("你sb吧，别乱输入")




