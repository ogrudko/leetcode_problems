'''
Problem:
Given a string s consists of some words separated by spaces,
return the length of the last word in the string. If the last word does not exist, return 0.
A word is a maximal substring consisting of non-space characters only.
'''

# Solution

class Solution:
    '''Solution for supposed problem'''
    @classmethod
    def length_of_last_word(cls, user_string: str) -> int:
        '''
        Returns the length of last word in a string.
        '''
        user_string = user_string.lstrip(' ')
        user_string = user_string.rstrip(' ')
        words = user_string.split(' ')
        if user_string == '':
            return 0
        return len(words[-1])



solution = Solution()
print(solution.length_of_last_word('Hello World')) # 5
print(solution.length_of_last_word(' ')) # 0
print(solution.length_of_last_word('a ')) # 1
