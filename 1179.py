par = impar = []
for _ in range(15):
    X = int(input())
    if X % 2 == 0:
        if len(par) == 5:
            for _ in range(len(par)):
                print(f"par[{_}] = {par[_]}")
            par.clear()
        par.append(X)
    else:
        if len(impar) == 5:
            for _ in range(len(impar)):
                print(f"impar[{_}] = {impar[_]}")
            impar.clear()
        impar.append(X)

for _ in range(len(impar)):
    print(f"impar[{_}] = {impar[_]}")
for _ in range(len(par)):
    print(f"par[{_}] = {par[_]}")

#---------------------------------------------------------------
# par = []
# impar = []
# for _ in range(15):
#     X = int(input())
#     lista = par if X % 2 == 0 else impar
#     lista.append(X)
#     if len(lista) == 5:
#         for i, v in enumerate(lista):
#             print(f"{'par' if lista == par else 'impar'}[{i}] = {v}")
#         lista.clear()

# for nome, lista in [("impar", impar), ("par", par)]:
#     for i, v in enumerate(lista):
#         print(f"{nome}[{i}] = {v}")