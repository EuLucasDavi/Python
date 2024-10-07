def calcular_media():
    while True:
        notas = []

        for i in range(1, 3):
            while True:
                nota = float(input())
                if 0.0 <= nota <= 10.0:
                    notas.append(nota)
                    break
                else:
                    print("nota invalida")

        media = sum(notas) / len(notas)
        print(f"media = {media:.2f}")
        print("novo calculo (1-sim 2-nao)")

        while True:
            opcao = int(input())
            if opcao == 1:
                break 
            elif opcao == 2:
                return 
            else:
                print("novo calculo (1-sim 2-nao)")

calcular_media()
