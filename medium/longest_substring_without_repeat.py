'''
Problem:
Given a string s, find the length of the longest substring without repeating characters.

Constraints:
0 <= s.length <= 5 * 10**4
s consists of English letters, digits, symbols and spaces.
'''
 
# Solution

class Solution:
    '''Class is needed to solve the abovementioned problem'''
    def length_of_longest_substring(self, s: str) -> int:
        '''
        Method finds the length of the longest substring without repeating characters

        Input:
        String: 0 <= s.length <= 5 * 10**4

        Returns:
        Integer: 

        Example 1:
        Input: s = "abcabcbb"
        Output: 3
        Explanation: The answer is "abc", with the length of 3.

        Example 2:
        Input: s = "bbbbb"
        Output: 1
        Explanation: The answer is "b", with the length of 1.

        Example 3:
        Input: s = "pwwkew"
        Output: 3
        Explanation: The answer is "wke", with the length of 3.
        Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

        Example 4:
        Input: s = ""
        Output: 0
        '''
        used_chars = {}
        substring = [] 
        length_longest_substring = 0
        if len(s) == 0:
            return 0
        else:            
            for char in s:
                if char not in used_chars:
                    substring += char
                    used_chars[char] = 1
                else:
                    if substring[0] == char:
                        substring.pop(0)
                        substring += char
                    else:
                        substring = substring[(substring.index(char) + 1):]
                        used_chars = {}
                        substring += char
                        used_chars[char] = 1
                if len(substring) > length_longest_substring:
                    length_longest_substring  = len(substring)
            return length_longest_substring
 

solution = Solution()
print(solution.length_of_longest_substring('qblqcb'))

