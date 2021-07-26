'''
Problem: 
Given a non-empty array of decimal digits representing a non-negative integer, increment one to the integer.
The digits are stored such that the most significant digit is at the head of the list, and each element in the array contains a single digit.
You may assume the integer does not contain any leading zero, except the number 0 itself.
'''

# Solution

class Solution:
    def plusOne(self, digits):
        i = 1
        plus_one = 1
        while plus_one == 1 and i <= len(digits):
            digits[-i] += plus_one
            if digits[-i] == 10:
                digits[-i] = 0
                plus_one += 1
            plus_one -= 1
            i += 1
        if plus_one == 1:
            digits.insert(0, 1)
            plus_one = 0
        return digits

solution = Solution()
print(solution.plusOne([1,2,3]))    # [1,2,4]
print(solution.plusOne([4,3,2,1]))    # [4,3,2,2]
print(solution.plusOne([0]))    # [1]
print(solution.plusOne([9]))    # [1, 0]
print(solution.plusOne([9, 9]))    # [1, 0, 0 ]
print(solution.plusOne([9, 9, 9]))    # [1, 0, 0, 0]
print(solution.plusOne([9, 9, 9, 9]))    # [1, 0, 0, 0, 0]
