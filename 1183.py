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
    res.append(matriz[i][i+1:])
res2 = []
if O == 'S':
    for i in res:
        res2.append(sum(i))
    print(f"{sum(res2):.1f}")
elif O == "M":
    for i in res:
        res2.append(sum(i))
    print(f"{sum(res2) / 66:.1f}")

#------------------------------------------------
# O = input()  # Recebe operação ('S' para soma, 'M' para média)

# # Recebe a matriz 12x12 como entrada
# matriz = [[float(input()) for _ in range(12)] for _ in range(12)]

# # Seleciona os elementos acima da diagonal principal
# elementos_acima_diagonal = [matriz[i][i+1:] for i in range(12)]

# # Achata a lista para facilitar cálculos
# elementos_flat = [elem for sublist in elementos_acima_diagonal for elem in sublist]

# # Realiza a operação com base no valor de 'O'
# resultado = sum(elementos_flat) if O == 'S' else sum(elementos_flat) / len(elementos_flat)

# # Exibe o resultado formatado com uma casa decimal
# print(f"{resultado:.1f}")