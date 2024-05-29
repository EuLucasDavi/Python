nums = []
while True:
    inp = list(map(int, input().split()))
    if any(x <= 0 for x in inp):
        break
    nums.append(inp)
for num in nums:
    odd_numbers = [x for x in range(min(num), max(num) + 1)]
    string_numbers = ' '.join(map(str, odd_numbers))
    print(f'{string_numbers} Sum={sum(odd_numbers)}')

# --------- Lembrar do Join e entender como funciona o any