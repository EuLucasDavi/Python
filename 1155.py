a = 0
for i in range(1, 101):
    S = 1/i
    a += S
print(f"{a:.2f}")

#-------------------------------------------
#print(f"{sum(1/i for i in range(1, 101)):.2f}")