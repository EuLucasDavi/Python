n = int(input())
a, b = 0, 1
for i in range(n):
    if i == 0:
        print(a, end="")
    else:
        print(" " + str(b), end="")
        a, b = b, a + b
print()