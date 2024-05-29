nums = []
while True:
    inp = list(map(int, input().split()))
    if any(inp.count(x) > 1 for x in inp):
        print("Dois números iguais foram inseridos. Parando a entrada de dados.")
        break
    nums.append(inp)
print(nums)
