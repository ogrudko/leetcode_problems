'''
Problem:
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
You must write an algorithm with O(log n) runtime complexity.
'''

# Solution

import bisect

class Solution:
    def search_insert(self, nums, target):
        if type(target) is int:
            return bisect.bisect_left(nums, target)
        return -1


