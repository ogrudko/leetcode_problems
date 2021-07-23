'''
Problem:
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
'''

# Solution

class Solution:
    def maxSubArray(self, nums) -> int:
        max_sub = nums[0]
        current_sum = 0
        for n in nums:
            if current_sum < 0:
                current_sum = 0
            current_sum += n
            max_sub = max(max_sub, current_sum)
        return max_sub

solution = Solution()
print(solution.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])) # 6
print(solution.maxSubArray([1])) # 1
print(solution.maxSubArray([5,4,-1,7,8])) # 23