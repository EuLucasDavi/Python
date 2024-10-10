gas = [0,0,0]
while True:
    entrada = int(input())
    if (entrada == 1):
        gas[0] += 1
    elif (entrada == 2):
        gas[1] += 1
    elif (entrada == 3):
        gas[2] += 1
    elif(entrada == 4):
        break
    else:
        continue
print(f"MUITO OBRIGADO\nAlcool: {gas[0]}\nGasolina: {gas[1]}\nDiesel: {gas[2]}")
# ---------------------------------------------------------------------------------------
# gas = [0, 0, 0]
# while (entrada := int(input())) != 4:
#     if 1 <= entrada <= 3:
#         gas[entrada - 1] += 1
# print(f"MUITO OBRIGADO\nAlcool: {gas[0]}\nGasolina: {gas[1]}\nDiesel: {gas[2]}")
