nums = [3, 9, 2, 7]
best = nums[0]
for n in nums:
    if n > best:
        best = n
print(best)
