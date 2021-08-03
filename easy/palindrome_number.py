'''
Problem:
Given an integer x, return true if x is palindrome integer.
An integer is a palindrome when it reads the same backward as forward. 
For example, 121 is palindrome while 123 is not.
Constraints:
-2^31 <= x <= 2^31 - 1
'''

class Solution:
    def is_palindrome(self, x):
        if type(x) != int:
            return False
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        elif x == 0:
            return True
        else:
            reverted_number = 0
            while x // 1 > reverted_number:
                reverted_number = reverted_number * 10 + x % 10
                x /= 10
                x = int(x)
            return x == reverted_number or x == reverted_number // 10


solution = Solution()
print(solution.is_palindrome(121))
print(solution.is_palindrome(33))