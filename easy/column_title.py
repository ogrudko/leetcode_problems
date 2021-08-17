'''
Problem:
Given an integer columnNumber,
return its corresponding column title as it appears in an Excel sheet.

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

Input: columnNumber = 1
Output: "A"
Example 2:

Input: columnNumber = 28
Output: "AB"
Example 3:

Input: columnNumber = 701
Output: "ZY"
Example 4:

Input: columnNumber = 2147483647
Output: "FXSHRXW"

Constraints:

1 <= columnNumber <= 2^31 - 1
'''

# Solution

class Solution:
    def convert_to_title(self, column_number: int) -> str:
        table = {
            1: 'A',
            2: 'B',
            3: 'C',
            4: 'D',
            5: 'E',
            6: 'F',
            7: 'G',
            8: 'H',
            9: 'I',
            10: 'J',
            11: 'K',
            12: 'L',
            13: 'M',
            14: 'N',
            15: 'O',
            16: 'P',
            17: 'Q',
            18: 'R',
            19: 'S',
            20: 'T',
            21: 'U',
            22: 'V',
            23: 'W',
            24: 'X',
            25: 'Y',
            26: 'Z'
        }
        output = ''
        while column_number > 0:
            trailing_letter = column_number % 26
            if trailing_letter != 0:
                output = table[trailing_letter] + output
                column_number //=26
            else:
                output = table[26] + output
                column_number = column_number // 26 - 1
        return output
