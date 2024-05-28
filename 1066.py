nums = [int(input()) for _ in range(5)]
soma = 0
positivos = 0
negativos = 0
for num in nums:
    if num % 2 == 0:
        soma +=1
    if num > 0:
        positivos +=1
    if num < 0: 
        negativos +=1
print(f'{soma} valor(es) par(es)')
print(f'{len(nums) - soma} valor(es) impar(es)')
print(f'{positivos} valor(es) positivo(s)')
print(f'{negativos} valor(es) negativo(s)')

#------------------------------------------------------
# nums = [int(input()) for _ in range(5)]
# pares = sum(1 for num in nums if num % 2 == 0)
# positivos = sum(1 for num in nums if num > 0)
# negativos = sum(1 for num in nums if num < 0)

# print(f'{pares} valor(es) par(es)')
# print(f'{len(nums) - pares} valor(es) impar(es)')
# print(f'{positivos} valor(es) positivo(s)')
# print(f'{negativos} valor(es) negativo(s)')

#------------------------------------------------------
# nums = [int(input()) for _ in range(5)]
# pares = sum(1 for num in nums if num % 2 == 0)
# print(f'{pares} valor(es) par(es)')
# print(f'{len(nums) - pares} valor(es) impar(es)')
# print(f'{sum(1 for num in nums if num > 0)} valor(es) positivo(s)')
# print(f'{sum(1 for num in nums if num < 0)} valor(es) negativo(s)')