num1 = int(input())
num2 = int(input())
if num1 <= num2:
    if num1 % 2 == 0:
        nums = list(range(num1 + 1,num2,2))
    else:
        nums = list(range(num1 + 2,num2,2))
else:
    if num2 % 2 == 0:
        nums = list(range(num2 + 1,num1,2))
    else:
        nums = list(range(num2 + 2,num1,2))
print(sum(nums))

#----------------------------
# num1 = int(input())
# num2 = int(input())
# start = min(num1, num2) + 1
# end = max(num1, num2)
# if start % 2 == 0:
#     start += 1
# nums = list(range(start, end, 2))
# print(sum(nums))