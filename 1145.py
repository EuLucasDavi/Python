x, y = map(int, input().split())

for i in range(1, y + 1, x):
    print(" ".join(str(j) for j in range(i, min(i + x, y + 1))))