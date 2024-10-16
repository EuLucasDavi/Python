S = res = 1
num = 3
den = 2
while num != 39:
    res = num / den
    S += res
    num += 2
    den *= 2
S = round(S)
print(f"{S:.2f}")