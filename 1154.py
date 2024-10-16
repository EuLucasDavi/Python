idades = []
while True:
    idade = int(input())
    if(idade > 0):
        idades.append(idade)
    else:
        break
soma = sum(idades) / len(idades)
print(f"{soma:.2f}")