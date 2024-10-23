while (N := int(input())) != 0:
    matriz = []
    for i in range(N):
        linha = [0] * N
        matriz.append(linha)
        for j in range(N):
            matriz[i][j] = 2 ** (i + j)
    maior_numero = matriz[N-1][N-1]
    T = len(str(maior_numero))
    for i in matriz:
        print(" ".join(f"{x:>{T}}" for x in i))
    print()