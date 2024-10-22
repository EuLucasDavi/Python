while True:
#     N = int(input())  # Lê a ordem da matriz
    
#     if N == 0:
#         break  # Se for 0, interrompe a execução

#     matriz = [[0] * N for _ in range(N)]  # Cria a matriz NxN

#     # Preenche a matriz de acordo com a lógica
#     for i in range(N):
#         for j in range(N):
#             matriz[i][j] = min(i + 1, j + 1, N - i, N - j)
    
#     # Imprime a matriz com formatação
#     for linha in matriz:
#         print(" ".join(f"{x:>3}" for x in linha))
    
#     print()  # Linha em branco após cada matriz