a = int(input())
b = int(input())
count = 0

init, end = (b, a) if a > b else (a, b)

valores = list(range(init, end + 1))

i = 0
for i in valores:
    res = valores[i] % 13
    if (res == 0):
        count +=1
print(count)