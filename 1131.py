grenais = 0
inter = 0
gremio = 0
empate = 0

while True:
    placar = input()
    numeros = list(map(int, placar.split()))
    grenais += 1
    if (numeros[0] > numeros[1]):
        inter += 1
    elif (numeros[0] < numeros[1]):
        gremio += 1
    else:
        empate += 1
    print("Novo grenal (1-sim 2-nao)")
    res = int(input())
    if (res == 1):
        continue
    else:
        champ = str
        if (inter > gremio):
            champ = "Inter venceu mais"
        elif (gremio > inter):
            champ = "Gremio venceu mais"
        else:
            champ = "Nao houve vencedor"
        print(f"{grenais} grenais\nInter:{inter}\nGremio:{gremio}\nEmpates:{empate}\n{champ}")
        break

# ---------------------------------------------------------------------------------------------------
# grenais = inter = gremio = empate = 0

# while True:
#     placar = list(map(int, input().split()))
#     grenais += 1
#     if placar[0] > placar[1]:
#         inter += 1
#     elif placar[0] < placar[1]:
#         gremio += 1
#     else:
#         empate += 1
#     print("Novo grenal (1-sim 2-nao)")
#     if int(input()) != 1:
#         champ = "Inter venceu mais" if inter > gremio else "Gremio venceu mais" if gremio > inter else "Nao houve vencedor"
#         print(f"{grenais} grenais\nInter:{inter}\nGremio:{gremio}\nEmpates:{empate}\n{champ}")
#         break
