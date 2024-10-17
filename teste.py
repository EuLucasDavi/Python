par = []
impar = []
for _ in range(15):
    X = int(input())
    if X % 2 == 0:
        if len(par) == 5:
            for i in range(len(par)):
                print(f"par[{i}] = {par[i]}")
            par.clear()
        par.append(X)
    else:
        if len(impar) == 5:
            for i in range(len(impar)):
                print(f"impar[{i}] = {impar[i]}")
            impar.clear()
        impar.append(X)

# Imprime os valores restantes nos vetores impar e par
for i in range(len(impar)):
    print(f"impar[{i}] = {impar[i]}")
for i in range(len(par)):
    print(f"par[{i}] = {par[i]}")
