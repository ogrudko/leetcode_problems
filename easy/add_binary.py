'''
Problem:
Given two binary strings a and b, return their sum as a binary string.
Constraints:
1 <= a.length, b.length <= 10^4
a and b consist only of '0' or '1' characters.
Each string does not contain leading zeros except for the zero itself.
'''

# Solution

class Solution:
    '''
    Solution for supposed problem
    '''
    def add_binary(self, first_binary: str, second_binary: str) -> str:
        '''
        Returns sum of binaries
        
        Parameters:
        a, b - binary numbers written as strings
        '''
        result = ""
        length_a = len(first_binary) - 1
        length_b = len(second_binary) - 1
        plus_one = 0
        while(length_a >= 0 or length_b >= 0):
            a1 = int(first_binary[length_a]) if length_a >= 0 else 0
            length_a -= 1
            b1 = int(second_binary[length_b]) if length_b >= 0 else 0
            length_b -= 1
            digit_sum = a1 + b1 + plus_one
            plus_one = 1 if digit_sum in (2, 3) else 0
            result += str(1 if digit_sum in (1, 3) else 0)
            print(result)
        if plus_one > 0:
            result += str(1)
        return result[::-1]



solution = Solution()
print(solution.add_binary("11", "1"))   # "100"
print(solution.add_binary("1", "11"))   # "100"
print(solution.add_binary("1010", "1011"))   # "10101"
