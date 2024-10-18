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
    for j in range(12):
        if i + j < 11 and j > i:
            res.append(matriz[i][j])
if O == 'S':
    resultado = sum(res)
    print(f"{resultado:.1f}")
elif O == "M":
    resultado = sum(res) / len(res)
    print(f"{resultado:.1f}")