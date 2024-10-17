qtd = int(input())
res = []
for _ in range(qtd):
    values = list(map(float, input().split()))
    values[0], values[1] = int(values[0]), int(values[1])
    anos = 0
    while values[0] <= values[1] and anos <= 100:
        values[0] += int(values[0] * (values[2]/100))
        values[1] += int(values[1] * (values[3]/100))
        anos += 1
    if anos <= 100:
        res.append(f"{anos} anos.")
    else:
        res.append("Mais de 1 seculo.")
print(*res, sep = "\n")

# :: Está apresentando RunTime Error --------------------------
# -------------------------------------------------------------
# T = int(input())  # Número de casos de teste

# for _ in range(T):
#     PA, PB, G1, G2 = input().split()
#     PA = int(PA)
#     PB = int(PB)
#     G1 = float(G1)
#     G2 = float(G2)

#     anos = 0

#     # Simulação do crescimento
#     while PA <= PB and anos <= 100:
#         PA += int(PA * (G1 / 100))  # População de A cresce em G1%
#         PB += int(PB * (G2 / 100))  # População de B cresce em G2%
#         anos += 1

#     # Se exceder 100 anos, exibir "Mais de 1 seculo."
#     if anos > 100:
#         print("Mais de 1 seculo.")
#     else:
#         print(f"{anos} anos.")
