qtd = int(input())
res = []
for i in range(qtd):
    entrada = int(input())
    nums = []
    num = entrada - 1
    while num > 0:
        if entrada % num == 0:
            nums.append(num)
        num -= 1
    if sum(nums) == entrada:
        res.append(f"{entrada} eh perfeito")
    else:
        res.append(f"{entrada} nao eh perfeito")
print(*res, sep = "\n")

#------------------------------------------------------
# qtd = int(input())
# res = []
# for _ in range(qtd):
#     entrada = int(input())
#     nums = [num for num in range(1, entrada) if entrada % num == 0]
#     res.append(f"{entrada} eh perfeito" if sum(nums) == entrada else f"{entrada} nao eh perfeito")
# print(*res, sep="\n")