'''
Problem:
Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.
In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

Example 1:

Input: rowIndex = 3
Output: [1,3,3,1]
Example 2:

Input: rowIndex = 0
Output: [1]
Example 3:

Input: rowIndex = 1
Output: [1,1]
 
Constraints:

0 <= rowIndex <= 33
'''

# Solution

class Solution:
    def get_row(self, row_index: int) -> list:
        pascal_triangle = [[]]
        for i in range(row_index + 1):
            for j in (range(i + 1)):
                if i in (0, 1) or j == 0 or i == j:
                    pascal_triangle[i].append(1)
                else:
                    pascal_triangle[i].append(pascal_triangle[i - 1][j - 1] + pascal_triangle[i - 1][j])
            pascal_triangle.append([])
        pascal_triangle.pop(-1)
        return pascal_triangle[-1]