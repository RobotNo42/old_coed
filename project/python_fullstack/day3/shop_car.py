items = ["Macbook", "剃须刀", "cherry", "ps4pro", "switch", "xboxone"]
price = [10000, 300, 1600, 2500, 3000, 2000]
buy_items = {}
total_money = int(input("输入你的工资"))
first_money = total_money
while True:
    print("你能买的东西如下")
    for i in range(len(items)):
        print(i+1, "\t",  items[i], "\t", (price[i]))
    num = input("输入你想要购买的商品编号,退出请输入q :").strip()
    if len(num) == 0:
        continue
    elif num.isdigit():
        num = int(num)
        if num < 1 or num > 6:
            print("请输入正确的编号")
        else:
            if total_money < price[int(num)-1]:
                print("你卡上钱不够，物品价格是", price[int(num)-1], "你还差", (price[int(num)-1]-total_money))
            else:
                if items[int(num)-1] in buy_items:
                    buy_items[items[num-1]][1] += 1
                else:
                    buy_items[items[num - 1]] = [price[num - 1], 1]
                total_money = total_money - price[num-1]
                print("购买成功，你的余额还剩", total_money)
    elif num == "q":
        if total_money == first_money:
            print("穷逼啥也不买，滚吧")
            break
        else:
            count = 1
            fina_money = 0
            print("---------你买了以下东西------------")
            print("序号 商品 数量 单价 总价 ")
            for x in buy_items:
                print("%s  %s  %s  %s  %s" % (count,
                      x,
                      buy_items[x][1],
                      buy_items[x][0],
                      buy_items[x][1] * buy_items[x][0]))
                count = count + 1
                fina_money += buy_items[x][1] * buy_items[x][0]
            print("总价格: %s" % fina_money)
            print("余额：", total_money)
            print("再见！")
            break
    else:
        print("你sb吧，别乱输入")
