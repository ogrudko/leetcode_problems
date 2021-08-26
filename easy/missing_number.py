'''
Problem:
Given an array nums containing n distinct numbers in the range [0, n],
return the only number in the range that is missing from the array.
Follow up: Could you implement a solution using only O(1) extra space complexity
and O(n) runtime complexity?

Constraints:
n == nums.length
1 <= n <= 10 ** 4
0 <= nums[i] <= n
All the numbers of nums are unique.
'''

# Solution

class Solution:
    '''
    class created to solve abovementioned problem.
    Holds only one method to find missing number in a list of integers
    '''
    def missing_number(self, nums: list) -> int:
        '''
        Method finds the missing integer in the list of integers according to the described problem.
        Parameters:
        nums : array of integers from 0 to n

        Returns : int

        Example 1:
        Input: nums = [3,0,1]
        Output: 2
        Explanation: n = 3 since there are 3 numbers, so all numbers are in the range [0,3].
        2 is the missing number in the range since it does not appear in nums.

        Example 2:
        Input: nums = [0,1]
        Output: 2
        Explanation: n = 2 since there are 2 numbers, so all numbers are in the range [0,2].
        2 is the missing number in the range since it does not appear in nums.

        Example 3:
        Input: nums = [9,6,4,2,3,5,7,0,1]
        Output: 8
        Explanation: n = 9 since there are 9 numbers, so all numbers are in the range [0,9].
        8 is the missing number in the range since it does not appear in nums.

        Example 4:
        Input: nums = [0]
        Output: 1
        Explanation: n = 1 since there is 1 number, so all numbers are in the range [0,1].
        1 is the missing number in the range since it does not appear in nums.
        '''
        if len(nums) == 1 and nums[0] == 0:
            return 1
        if 0 not in nums:
            return 0
        nums = sorted(nums)
        missing_number = len(nums)
        for i in range(len(nums) - 1):
            if nums[i + 1] - nums[i] > 1:
                missing_number = nums[i] + 1
        return missing_number
