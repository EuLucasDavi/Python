nums = []
for _ in range(20):
    nums.append(int(input()))
nums.reverse()
for _ in range(20):
    print(f"N[{_}] = {nums[_]}", sep = "\n")

# ------------------------------------
# # Inicializa o vetor com 20 posições
# N = []

# # Lê 20 valores inteiros do usuário
# for i in range(20):
#     valor = int(input())
#     N.append(valor)

# # Troca os elementos conforme a regra especificada
# for i in range(10):
#     N[i], N[19 - i] = N[19 - i], N[i]

# # Exibe o vetor modificado
# for i in range(20):
#     print(f"N[{i}] = {N[i]}")
