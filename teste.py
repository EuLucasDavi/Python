i = 0.0
j_values = [1.0, 2.0, 3.0]

while i <= 2:
    for j in j_values:
        i_rounded = round(i, 1)
        j_rounded = round(j, 1)
        i_str = f'{int(i_rounded)}' if i_rounded.is_integer() else f'{i_rounded:.1f}'
        j_str = f'{int(j_rounded)}' if j_rounded.is_integer() else f'{j_rounded:.1f}'
        print(f'I={i_str} J={j_str}')
    j_values = [x + 0.2 for x in j_values]
    i += 0.2