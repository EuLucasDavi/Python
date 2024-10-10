a, b = int(input()), int(input())

init, end = (b, a) if a > b else (a, b)

valores = list(range(init + 1, end))

for i in valores:
    if i % 5 == 2 or i % 5 == 3:
        print(i)

#------------------------------------------------
# x, y = int(input()), int(input())
# for i in range(min(x, y) + 1, max(x, y)):
#     if i % 5 in [2, 3]:
#         print(i)