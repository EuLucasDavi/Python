import math
while (N := list(map(int, input().split()))) != [0]:   
    area_casa = N[0] * N[1]
    lado_terreno = math.sqrt((area_casa * 100) / N[2])
    print(int(lado_terreno))