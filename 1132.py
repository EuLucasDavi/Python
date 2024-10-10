a = int(input())
b = int(input())
count = 0

init, end = (b, a) if a > b else (a, b)

valores = list(range(init, end + 1))

for i in valores:
    res = i % 13
    if (res != 0):
        count +=i
print(count)

#----------------------------------------------------
# a, b = int(input()), int(input())
# print(sum(i for i in range(min(a, b), max(a, b) + 1) if i % 13 != 0))