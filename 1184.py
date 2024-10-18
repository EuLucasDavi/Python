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
        if i > j:
            res.append(matriz[i][j])
if O == 'S':
    resultado = sum(res)
    print(f"{resultado:.1f}")
elif O == "M":
    resultado = sum(res) / len(res)
    print(f"{resultado:.1f}")

#------------------------------------------------
# O = input()  # Recebe operação ('S' para soma, 'M' para média)

# # Recebe a matriz 12x12 como entrada
# matriz = [[float(input()) for _ in range(12)] for _ in range(12)]

# # Seleciona os elementos abaixo da diagonal principal (i > j)
# elementos_inferior_diagonal = [matriz[i][j] for i in range(12) for j in range(i)]

# # Realiza a operação com base no valor de 'O'
# if O == 'S':
#     resultado = sum(elementos_inferior_diagonal)
# elif O == 'M':
#     resultado = sum(elementos_inferior_diagonal) / len(elementos_inferior_diagonal)

# # Exibe o resultado formatado com uma casa decimal
# print(f"{resultado:.1f}")

