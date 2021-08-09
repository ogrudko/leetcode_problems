'''
Problem:
Given a non-empty array of integers nums, every element appears twice except for one.
Find that single one.
You must implement a solution with a linear runtime complexity and use only constant extra space.
Example 1:

Input: nums = [2,2,1]
Output: 1
Example 2:

Input: nums = [4,1,2,1,2]
Output: 4
Example 3:

Input: nums = [1]
Output: 1

Constraints:

1 <= nums.length <= 3 * 104
-3 * 104 <= nums[i] <= 3 * 104
Each element in the array appears twice except for one element which appears only once.
'''

# Solution

class Solution:
    def single_number(self, nums) -> int:
        if len(nums) == 0 or not isinstance(nums, list):
            return 0
        hashmap = dict()
        for num in nums:
            if not isinstance(num, int):
                return -1
            if num not in hashmap.keys():
                hashmap[num] = 1
            else:
                del hashmap[num]
        single_number = hashmap.keys()
        if len(single_number) > 1:
            return -2
        if len(single_number) == 0:
            return 0
        return list(single_number)[0]
