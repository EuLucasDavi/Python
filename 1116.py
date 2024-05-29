qtd = int(input())
for _ in range(qtd):    
    nums = list(map(int,input().split()))
    if nums[1] != 0:
        print(f'{nums[0] / nums[1]:.1f}')
    else:
        print('divisao impossivel')

# ----------------------------------------------------#
# for _ in range(int(input())):    
#     nums = list(map(int, input().split()))
#     print(f'{nums[0] / nums[1]:.1f}' if nums[1] != 0 else 'divisao impossivel')