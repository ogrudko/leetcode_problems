'''
Problem:
Given a string s consists of some words separated by spaces, return the length of the last word in the string. If the last word does not exist, return 0.
A word is a maximal substring consisting of non-space characters only.
'''

# Solution

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.lstrip(' ')
        s = s.rstrip(' ')
        words = s.split(' ')
        if s == '':
            return 0
        else:
            return len(words[-1])



solution = Solution()
print(solution.lengthOfLastWord('Hello World')) # 5
print(solution.lengthOfLastWord(' ')) # 0
print(solution.lengthOfLastWord('a ')) # 1
