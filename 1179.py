par = impar = []
for _ in range(15):
    X = int(input())
    if X % 2 == 0:
        if len(par) == 5:
            for _ in range(len(par)):
                print(f"par[{_}] = {par[_]}")
            par.clear()
        else:
            par.append(X)
    else:
        if len(impar) == 5:
            for _ in range(len(impar)):
                print(f"par[{_}] = {impar[_]}")
            impar.clear()
        else:
            impar.append(X)

for _ in range(len(impar)):
    print(f"impar[{_}] = {impar[_]}")
for _ in range(len(par)):
    print(f"par[{_}] = {par[_]}")
