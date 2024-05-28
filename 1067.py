num = int(input())

if num < 1001 and num > 0:
    nums = list(range(1,num + 1))
    for num in nums:
        if num % 2 != 0:
            print(num)