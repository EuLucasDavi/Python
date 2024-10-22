while (N := int(input())) != 0:
    matriz = []
    for i in range(N):
        linha = [0] * N
        matriz.append(linha)
        for j in range(N):
            matriz[i][j] = abs(i - j) + 1
    for i in matriz:
        print(" ".join(f"{x:>3}" for x in i))
    print()