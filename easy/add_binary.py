'''
Problem:
Given two binary strings a and b, return their sum as a binary string.
Constraints:
1 <= a.length, b.length <= 104
a and b consist only of '0' or '1' characters.
Each string does not contain leading zeros except for the zero itself.
'''

# Solution

class Solution:
    def add_binary(self, a: str, b: str) -> str:
        c = ""
        length_a = len(a) - 1
        length_b = len(b) - 1
        plus_one = 0
        while(length_a >= 0 or length_b >= 0):
            a1 = int(a[length_a]) if length_a >= 0 else 0
            length_a -= 1
            b1 = int(b[length_b]) if length_b >= 0 else 0
            length_b -= 1
            sum = a1 + b1 + plus_one
            plus_one = 1 if sum == 3 or sum == 2 else 0
            c += str(1 if sum == 1 or sum == 3 else 0)
        if plus_one > 0:
            c += str(1)
        return c[::-1]



solution = Solution()
print(solution.add_binary("11", "1"))   # "100"
print(solution.add_binary("1", "11"))   # "100"
print(solution.add_binary("1010", "1011"))   # "10101"
