i = 1
j_values = [7, 6, 5]
while i <= 9:
    for j in j_values:
        print(f'I={i} J={j}')
    j_values = [x + 2 for x in j_values]
    i += 2