L = int(input())
O = input()

matriz = []
for i in range(12):
    linha = []
    for j in range(12):
        value = float(input())
        linha.append(value)
    matriz.append(linha)

if O == "S":
    print(f"{sum(matriz[L]):.1f}")
elif O == "M":
    print(f"{sum(matriz[L])/len(matriz[L]):.1f}")