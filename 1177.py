T = int(input())
N = []
while len(N) < 1000:
    for _ in range(T):
        N.append(_)
        if len(N) == 1000:
            break
for _ in range(len(N)):
    print(f"N[{_}] = {N[_]}")

#------------------------------------------------------
# T = int(input())
# N = [i for i in range(T)][:1000]
# for i in range(len(N)):
#     print(f"N[{i}] = {N[i]}")