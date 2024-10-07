def calcular_media():
    while True:
        notas = []

        # Lê as duas notas, validando separadamente
        for i in range(1, 3):
            while True:
                nota = float(input())
                if 0.0 <= nota <= 10.0:
                    notas.append(nota)
                    break
                else:
                    print("nota invalida")

        # Calcula e imprime a média
        media = sum(notas) / len(notas)
        print(f"media = {media:.2f}")
        print("novo calculo (1-sim 2-nao)")

        # Pergunta se o usuário deseja realizar um novo cálculo
        while True:
            opcao = int(input())
            if opcao == 1:
                break  # Reinicia o loop para um novo cálculo
            elif opcao == 2:
                return  # Encerra o programa
            else:
                print("novo calculo (1-sim 2-nao)")

# Chama a função para iniciar o programa
calcular_media()