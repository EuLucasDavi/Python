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

#----------------------------------------------
# # Leitura da linha a ser considerada e da operação (Soma ou Média)
# L = int(input())  # Número da linha (0 a 11)
# T = input()       # Operação ('S' para Soma, 'M' para Média)

# # Leitura da matriz 12x12
# matriz = []
# for i in range(12):
#     linha = []
#     for j in range(12):
#         valor = float(input())  # Leitura de um valor de ponto flutuante
#         linha.append(valor)
#     matriz.append(linha)

# # Seleciona a linha correspondente
# linha_escolhida = matriz[L]

# # Realiza a operação de acordo com a entrada
# if T == 'S':
#     resultado = sum(linha_escolhida)  # Soma dos elementos da linha
# elif T == 'M':
#     resultado = sum(linha_escolhida) / len(linha_escolhida)  # Média dos elementos da linha

# # Exibe o resultado com uma casa decimal
# print(f"{resultado:.1f}")