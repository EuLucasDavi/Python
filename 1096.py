i, j , controle, index, controle2= 1, [7,6,5], 0, 0, 3
while i <= 9:
    if index == 3:  
        index = 0
    print(f'I={i} J={j[index]}')
    controle += 1
    index += 1
    if controle >= controle2:
        i += 2
        controle2+=3

#-----------------------------------------------------------#
# i = 1
# j_values = [7, 6, 5]
# while i <= 9:
#     for j in j_values:
#         print(f'I={i} J={j}')
#     i += 2