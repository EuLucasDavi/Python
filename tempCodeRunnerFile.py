X = float(input())
nums = [X / (2 ** i) for i in range(100)]
print("\n".join(f"N[{i}] = {nums[i]:.4f}" for i in range(100)))