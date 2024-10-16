qtd = int(input())
res = []
for _ in range(qtd):
    values = list(map(float, input().split()))
    values[0], values[1] = int(values[0]), int(values[1])
    anos = 0
    while values[0] <= values[1] and anos <= 101:
        values[0] += round(values[0] * (values[2]/100))
        values[1] += round(values[1] * (values[3]/100))
        anos += 1
    if anos <= 100:
        res.append(f"{anos} anos.")
    else:
        res.append("Mais de 1 seculo.")
    qtd -= 1
print(*res, sep = "\n")

# :: Está apresentando RunTime Error --------------------------