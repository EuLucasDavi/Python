try:
    while (N := int(input())) != 0:
        matriz = []
        for i in range(N):
            linha = [0] * N
            matriz.append(linha)
            for j in range(N):
                if i == j:
                    matriz[i][j] = 1
                else:
                    matriz[i][j] = 3
        for _ in matriz:
            print(*_)
except EOFError:
    pass