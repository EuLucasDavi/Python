X = float(input())
nums = [X]
while len(nums) < 100:
    nums.append(X / 2)
    X /= 2
for _ in range(len(nums)):
    print(f"N[{_}] = {nums[_]:.4f}")

#----------------------------------------------------------
# X = float(input())
# nums = [X / (2 ** i) for i in range(100)]
# print("\n".join(f"N[{i}] = {nums[i]:.4f}" for i in range(100)))