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