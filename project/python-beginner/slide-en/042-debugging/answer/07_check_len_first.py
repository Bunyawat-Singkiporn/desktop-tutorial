n = int(input())
nums = []
for i in range(n):
    nums.append(int(input()))
if len(nums) == 0:
    print("Empty")
else:
    print(nums[-1])
