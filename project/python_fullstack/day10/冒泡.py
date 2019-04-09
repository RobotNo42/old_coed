def my_sort(num):
    l = len(num)
    for i in range(l-1):
        for j in range(l-1-i):
            if num[j] < num[j+1]:
                num[j], num[j+1] = num[j+1], num[j]


nums = [2,45,67,8,0,56]
print(nums)
my_sort(nums)
print(nums)
