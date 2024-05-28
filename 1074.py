num = int(input())
nums = []
for _ in range(num):
    a = int(input())
    nums.append(a)
for numero in nums:
    if numero % 2 == 0 and numero > 0:
        print('EVEN POSITIVE')
    if numero % 2 == 0 and numero < 0:
        print('EVEN NEGATIVE')
    if numero % 2 != 0 and numero > 0:
        print('ODD POSITIVE')
    if numero % 2 != 0 and numero < 0:
        print('ODD NEGATIVE')
    if numero == 0:
        print('NULL')

#--------------------------------------------------------#
# num = int(input())
# nums = [int(input()) for _ in range(num)]

# for numero in nums:
#     if numero == 0:
#         print('NULL')
#     elif numero % 2 == 0:
#         if numero > 0:
#             print('EVEN POSITIVE')
#         else:
#             print('EVEN NEGATIVE')
#     else:
#         if numero > 0:
#             print('ODD POSITIVE')
#         else:
#             print('ODD NEGATIVE')
