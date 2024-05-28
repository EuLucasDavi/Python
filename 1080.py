n , index = 0 , 0
for _ in range(100):
    a = int(input())
    if a > n:
        n = a
        index = _ + 1
print(f'{n}\n{index}')

#-------------------------------------#
# n, index = max((int(input()), i + 1) for i in range(100))
# print(f'{n}\n{index}')
