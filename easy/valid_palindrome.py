'''
Problem:
Given a string s, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
'''

# Solution

class Solution:
    def is_palindrome(self, s):
        our_list = []
        our_list[:0] = s
        while len(our_list) > 1:
            while not our_list[0].isalnum() and  len(our_list) > 1:
                our_list.pop(0)
            while not our_list[-1].isalnum() and len(our_list) > 1:
                our_list.pop()
            if our_list[0].lower() != our_list[-1].lower():
                return False
            else:
                if len(our_list) > 0:
                    our_list.pop(0)
                if len(our_list) > 0:
                    our_list.pop(-1)
        return True

solution = Solution()
print(solution.is_palindrome(',.'))