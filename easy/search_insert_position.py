'''
Problem:
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
You must write an algorithm with O(log n) runtime complexity.
'''

# Solution

import bisect

class Solution:
    def searchInsert(self, nums, target):
        return bisect.bisect_left(nums, target)


solution = Solution()
print(solution.searchInsert([1,3,5,6], 5)) # 2
print(solution.searchInsert([1,3,5,6], 2)) # 1
print(solution.searchInsert([1,3,5,6], 7)) # 4
print(solution.searchInsert([1,3,5,6], 0)) # 0
print(solution.searchInsert([1], 0)) #       0
print(solution.searchInsert([1,3,5], 4)) #   2
print(solution.searchInsert([2,7,8,9,10], 9)) # 3