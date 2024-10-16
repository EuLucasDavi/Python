res = []
while (entrada := int(input())) != 0:
    if entrada % 2 != 0:
        entrada += 1
    res.append(sum(entrada + 2 * i for i in range(5)))
print(*res, sep='\n')