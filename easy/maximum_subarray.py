'''
Problem:
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
'''

# Solution

class Solution:
    def max_sub_array(self, nums) -> int:
        max_sub = nums[0]
        current_sum = 0
        for n in nums:
            if current_sum < 0:
                current_sum = 0
            current_sum += n
            max_sub = max(max_sub, current_sum)
        return max_sub

