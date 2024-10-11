while True:
    entrada = input().split()
    A = int(entrada[0])
    res = 0
    for i in entrada[1:]:
        i = int(i)
        if i > 0:
            N = i
    for i in range(0, N):
        res = res + A + i
    print(res)
    break