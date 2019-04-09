def age(x):
    if x == 0:
        return 10
    else:
        return age(x-1)+2

print(age(1))