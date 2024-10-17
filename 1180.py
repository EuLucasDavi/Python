N = int(input())
nums = list(map(int, input().split()))[:N]
menor = nums[0]
index = 0
for i in nums:
    if i < menor:
        menor = i
        index = nums.index(menor)
print(f"Menor valor: {menor}\nPosicao: {index}")

#-------------------------------------------
# N = int(input())  # Número de elementos
# nums = list(map(int, input().split()))[:N]  # Lista de números

# menor_valor = nums[0]  # Inicializa o menor valor
# indice_menor = 0  # Inicializa o índice do menor valor

# # Percorre a lista, começando do segundo elemento
# for i in range(1, N):
#     if nums[i] < menor_valor:
#         menor_valor = nums[i]
#         indice_menor = i

# # Exibe o menor valor e sua posição
# print(f"Menor valor: {menor_valor}\nPosicao: {indice_menor}")
