C = int(input())
O = input()

matriz = []
for i in range(12):
    linha = []
    for j in range(12):
        value = float(input())
        linha.append(value)
    matriz.append(linha)
res = []
for i in range(12):
    res.append(matriz[i][C])
if O == 'S':
    print(f"{sum(res):.1f}")
elif O == "M":
    print(f"{sum(res) / len(res):.1f}")