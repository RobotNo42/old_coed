name = {12, 32, 23, 45, 123, 4654, 1231, 1, 2, 212, 56, 9, 34, 99, 30}
name_sor = sorted(name)


def second_find(x, li):
    mid_index = int(len(li) / 2)
    if len(li) > 1:
        if x > li[mid_index]:
            l1 = li[mid_index:]
            second_find(x,l1)
        elif x <li[mid_index]:
            l2 = li[:mid_index]
            second_find(x,l2)
        else:
            print('恭喜你找到了')
    elif len(li) == 1:
        if li[0] == x:
            print("恭喜你找到了")
        else:
            print("gun!")


second_find(22, name_sor)

