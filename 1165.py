qtd = int(input())
res = []
for _ in range(qtd):
    entrada = int(input())
    eh_primo = True
    for i in range(2, int(entrada**0.5) + 1):
        if entrada % i == 0:
            eh_primo = False 
            break

    if eh_primo:
        res.append(f"{entrada} eh primo")
    else:
        res.append(f"{entrada} nao eh primo")
print(*res, sep = "\n")

# -------------------------------------
# def eh_primo(n):
#     if n <= 1:
#         return False
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             return False
#     return True

# # Solicita um número ao usuário
# numero = int(input("Digite um número inteiro: "))

# # Verifica se o número é primo e exibe o resultado
# if eh_primo(numero):
#     print(f"{numero} é primo.")
# else:
#     print(f"{numero} não é primo.")
