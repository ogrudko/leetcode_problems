'''
Problem:
Given a string s, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
'''

# Solution

class Solution:
    def is_palindrome(self, s):
        our_list = []
        our_list[:0] = s
        for i in range(len(our_list)):
            if our_list[i].isalpha() == False:
                our_list.pop(i)
        print(our_list)

solution = Solution()
solution.is_palindrome('A man, a plan, a canal: Panama')    # true
solution.is_palindrome('raceacar')  # false