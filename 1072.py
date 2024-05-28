dentro = 0
fora = 0
qtd = int(input())
for _ in range(qtd):
    a = int(input())
    if 10 <= a <= 20:
        dentro += 1
    else:
        fora += 1
print(f'{dentro} in')
print(f'{fora} out')