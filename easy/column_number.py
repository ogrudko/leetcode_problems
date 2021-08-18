'''
Problem:
Given a string column_title that represents
the column title as appear in an Excel sheet, 
return its corresponding column number.

For example:

A -> 1
B -> 2
C -> 3
...
Z -> 26
AA -> 27
AB -> 28 
...

Example 1:
Input: columnTitle = "A"
Output: 1

Example 2:
Input: columnTitle = "AB"
Output: 28

Example 3:
Input: columnTitle = "ZY"
Output: 701

Example 4:
Input: columnTitle = "FXSHRXW"
Output: 2147483647
'''

# Solution

class Solution:
    def title_to_number(self, column_title: str) -> int:
        conversion_table = {
            'A': 1,
            'B': 2,
            'C': 3,
            'D': 4,
            'E': 5,
            'F': 6,
            'G': 7,
            'H': 8,
            'I': 9,
            'J': 10,
            'K': 11,
            'L': 12,
            'M': 13,
            'N': 14,
            'O': 15,
            'P': 16,
            'Q': 17,
            'R': 18,
            'S': 19,
            'T': 20,
            'U': 21,
            'V': 22,
            'W': 23,
            'X': 24,
            'Y': 25,
            'Z': 26
        }
        output = 0
        if not isinstance(column_title, str):
            return -1
        column_title = [letter for letter in column_title]
        power = 0
        while len(column_title) > 0:
            trailing_letter = column_title[-1]
            if not trailing_letter.isalpha():
                return -1
            if output > 0:
                output += conversion_table[trailing_letter] * (26 ** power)
            else:
                output += conversion_table[trailing_letter]
            column_title.pop()
            power += 1
        return output
