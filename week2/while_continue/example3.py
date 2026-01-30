nums = [5, -2, 7, -1, 3]
i = 0

while i < len(nums):
    if nums[i] < 0:
        i += 1
        continue
    print(nums[i])
    i += 1
