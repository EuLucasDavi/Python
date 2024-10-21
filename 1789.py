try:
    while True:
        N = int(input())
        vel = list(map(int, input().split()))[:N]
        vel.sort()
        if vel[-1] < 10:
            print(1)
        elif vel[-1] < 20:
            print(2)
        else:
            print(3)
except EOFError:
    pass