total,c,s,r = 0,0,0,0

entrada = int(input())
for _ in range(entrada):
    a = input().split()
    total += int(a[0])
    if a[1] == 'C':
        c = c + int(a[0])
    elif a[1] == 'R':
        r = r + int(a[0])
    else:
        s = s + int(a[0])

print(f'Total: {total} cobaias\nTotal de coelhos: {c}\nTotal de ratos: {r}\nTotal de sapos: {s}\nPercentual de coelhos: {c/total*100:.2f} %\nPercentual de ratos: {r/total*100:.2f} %\nPercentual de sapos: {s/total*100:.2f} %')

#----------------------------------------------------------------#
# total, c, r, s = 0, 0, 0, 0

# for _ in range(int(input())):
#     quantidade, tipo = input().split()
#     quantidade = int(quantidade)
#     total += quantidade
#     if tipo == 'C':
#         c += quantidade
#     elif tipo == 'R':
#         r += quantidade
#     else:
#         s += quantidade

# print(f'Total: {total} cobaias')
# print(f'Total de coelhos: {c}')
# print(f'Total de ratos: {r}')
# print(f'Total de sapos: {s}')
# print(f'Percentual de coelhos: {c / total * 100:.2f} %')
# print(f'Percentual de ratos: {r / total * 100:.2f} %')
# print(f'Percentual de sapos: {s / total * 100:.2f} %')