'''
Problem:
Implement strStr().
Return the index of the first occurrence of needle in haystack,
or -1 if needle is not part of haystack.
'''

class Solution:
    '''solution for the proposed problem'''
    def str_str(self, haystack, needle):
        '''
        Returns the index of needle's first occurence in a haystack
        Arguments:
        haystack (str) - string we use to find a needle
        needle (str) - substring index if which we want to find in the haystack
        '''

        if needle == "" or haystack == "":
            return 0
        if needle not in haystack:
            return -1
        return haystack.find(needle)

solution = Solution()
print(solution.str_str("hello world", "wo")) # 6
