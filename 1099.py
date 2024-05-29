qtd = int(input())
nums = [(list(map(int, input().split()))) for _ in range(qtd)]
for num in nums:
    a = list(range(min(num) + 1,max(num)))
    for _ in a:
        if _ % 2 == 0:
            a.remove(_)
    print(sum(a))

#--------------------------------------------------------------#
# qtd = int(input())
# nums = [list(map(int, input().split())) for _ in range(qtd)]

# for num in nums:
#     min_num, max_num = min(num), max(num)
#     odd_numbers = [x for x in range(min_num + 1, max_num) if x % 2 != 0]
#     print(sum(odd_numbers))
