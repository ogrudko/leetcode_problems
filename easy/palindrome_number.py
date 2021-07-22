'''
Problem:
Given an integer x, return true if x is palindrome integer.
An integer is a palindrome when it reads the same backward as forward. 
For example, 121 is palindrome while 123 is not.
Constraints:
-2^31 <= x <= 2^31 - 1
'''

class Solution:
    def isPalindrome(self, x):
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        elif x == 0:
            return True
        else:
            reverted_number = 0
            while x > reverted_number:
                reverted_number = reverted_number * 10 + x % 10
                x /= 10
            return x == reverted_number or x == reverted_number / 10


solution = Solution()
print(solution.isPalindrome(121))