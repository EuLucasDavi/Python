qtd = int(input())
res = []
for _ in range(qtd):
    values = list(map(float, input().split()))
    values[0], values[1] = int(values[0]), int(values[1])
    anos = 0
    while values[0] <= values[1] and anos <= 100:  # Limite de 100 anos
        values[0] += int(values[0] * (values[2] / 100))  # Trunca o crescimento
        values[1] += int(values[1] * (values[3] / 100))  # Trunca o crescimento
        anos += 1
    if anos <= 100:
        res.append(f"{anos} anos.")
    else:
        res.append("Mais de 1 seculo.")
print(*res, sep="\n")
