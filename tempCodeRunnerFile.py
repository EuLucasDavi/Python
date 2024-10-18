O = input()

matriz = []
for i in range(3):
    linha = []
    for j in range(3):
        value = float(input())
        linha.append(value)
    matriz.append(linha)
res = []
for i in range(3):
    res.append(matriz[i][i+1:])
res2 = []
for i in res:
    res2.append(i)
print(res2)