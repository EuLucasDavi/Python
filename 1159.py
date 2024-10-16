res = []
while True:
    entrada = int(input())
    if entrada == 0:
        break
    soma = []
    while len(soma) < 5:
        if entrada % 2 == 0:
            soma.append(entrada)
        entrada += 1
    res.append(sum(soma))
print(*res, sep='\n')

#-------------------------------------------------------
# res = []
# while (entrada := int(input())) != 0:
#     if entrada % 2 != 0:
#         entrada += 1
#     res.append(sum(entrada + 2 * i for i in range(5)))
# print(*res, sep='\n')