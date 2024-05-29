nums = []
while True:
    inp = list(map(int, input().split()))
    if any(inp.count(x) > 1 for x in inp):
        break
    nums.append(inp)
for num in nums:
    if num[0] < num[1]:
        print('Crescente')
    else:
        print('Decrescente')

# Método count() é aplicado em uma lista e o parâmetro passado é contado e retonnado em Int de acordo com a
# quantidade de vezes que ele aparece na lista onde foi aplicado o método