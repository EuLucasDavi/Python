nums = []

for _ in range(5):
    num = int(input())
    if num % 2 == 0:
        nums.append(num)

print(str(len(nums)) + " valores pares")

# nums = [int(input()) for _ in range(5) if int(input()) % 2 == 0]
# print(f"{len(nums)} valores pares")
