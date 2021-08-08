'''
Problem:
Given an array nums of size n, return the majority element.
The majority element is the element that appears more than ⌊n / 2⌋ times. 
You may assume that the majority element doesn't always exists in the array.
'''

# Solution

class Solution:
    def majority_element(self, nums) -> int:
        hashmap = {}
        if len(nums) == 0:
            return 0
        for element in nums:
            if element not in hashmap:
                hashmap[element] = 1
            else:
                hashmap[element] += 1
        values = hashmap.values()
        max_value = max(values)
        for key in hashmap:
            if hashmap[key] == max_value and max_value > (len(nums) / 2):
                return key
        return 0