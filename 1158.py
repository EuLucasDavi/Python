qtd = int(input())
res = []
a = []
for i in range(0,qtd):
    entrada = list(map(int, input().split()))
    num = entrada[0]
    while len(a) < entrada[1]:
        if num % 2 != 0:
            a.append(num)
        num += 1
    res.append(sum(a))
    a = []
for i in res:
    print(i)

#--------------------------------------------------------
# qtd = int(input())
# res = []

# for _ in range(qtd):
#     num, count = map(int, input().split())
#     a = [n for n in range(num, num + 2 * count) if n % 2 != 0][:count]
#     res.append(sum(a))

# print(*res, sep='\n')