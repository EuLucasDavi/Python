X = int(input())
Y = -1
res = X
count = 1
while (Y <= X):
    Y = int(input())
while res <= Y:
    X += 1
    res = res + X
    count += 1
print(count)