try:
    while True:
        N = int(input())
        vf = 0
        vel = list(map(int, input().split()))[:N]
        vel.sort()
        if vel[-1] < 10:
            vf = 1
        elif 10 <= vel[-1] < 20:
            vf = 2
        else:
            vf = 3
        print(vf)
except KeyboardInterrupt:
    pass