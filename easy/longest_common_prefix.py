'''
Problem:
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".
Constraints:
1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lower-case English letters.
'''

# Solution

class Solution:
    def longestCommonPrefix(self, strs):
        if len(strs):
            current_letter = strs[0][0]
            is_common = True
            longest_common_prefix = ""
            shortest_string = min(strs, key=len) # compare prefixes with the shortest string to avoid out of range errors
            for j in range(len(shortest_string)):   # iterate through the letters of shortest strings
                for i in range(len(strs)):  # iterate through strings comparing letters of the same index
                    current_letter = strs[0][j]
                    if current_letter != strs[i][j]:
                        is_common = False
                if is_common:
                    longest_common_prefix += current_letter
                is_common = True
            return longest_common_prefix
        else:
            return ""

solution = Solution()
print(solution.longestCommonPrefix(["flower","flow","flight"]))   # "fl"
print(solution.longestCommonPrefix(["dog","racecar","car"]))    # ""


