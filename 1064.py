entries = []

for i in range(6):
    num = float(input())
    if num >= 0:
        entries.append(num)

qtd = len(entries)
soma = sum(entries)

print( str(qtd) + " valores positivos")

print(f"{soma/qtd:.1f}")

# entries = [float(input()) for _ in range(6) if (num := float(input())) >= 0]

# qtd = len(entries)
# soma = sum(entries)

# print(f"{qtd} valores positivos")
# print(f"{soma/qtd:.1f}")