testes = int(input())
nums = []
for _ in range(testes):
    a = list(map(float, input().split()))
    a[0] *= 2
    a[1] *= 3
    a[2] *= 5
    nums.append(a)
for num in nums:
    print(f'{sum(num)/10:.1f}')

#------------------------------------------------------------#
# testes = int(input())
# nums = [(lambda x: x[0]*2 + x[1]*3 + x[2]*5)(list(map(float, input().split()))) for _ in range(testes)]
# for num in nums:
#     print(f'{num/10:.1f}')