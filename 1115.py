nums = []
while True:
    inp = list(map(int, input().split()))
    if any(x == 0 or x == None for x in inp):
        break
    nums.append(inp)
for num in nums:
    if num[0] > 0 and num[1] > 0:
        print('primeiro')
    elif num[0] < 0 and num[1] < 0:
        print('terceiro')
    elif num[0] > 0 and num[1] < 0:
        print('quarto')
    else:
        print('segundo')

# --------------------------------------------- #
# while True:
#     inp = list(map(int, input().split()))
#     if any(x == 0 or x is None for x in inp):
#         break
#     if inp[0] > 0:
#         print('primeiro' if inp[1] > 0 else 'quarto')
#     else:
#         print('segundo' if inp[1] > 0 else 'terceiro')