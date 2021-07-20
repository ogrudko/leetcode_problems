nums = [1,1,2]
i = 0
j = 0
k = 1
if len(nums) == 0:
    k = 0
else:
    while j < len(nums):
        if nums[j] != nums[i]:
            nums[i + 1] = nums[j]
            k += 1
            i += 1
        j += 1

print(k, nums)