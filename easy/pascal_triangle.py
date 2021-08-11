'''
Problem:
Given an integer numRows, return the first numRows of Pascal's triangle.
In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

Example 1:

Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
Example 2:

Input: numRows = 1
Output: [[1]]
 
Constraints:
1 <= numRows <= 30
'''

# Solution

class Solution:
    def generate(self, num_rows: int):
        pascal_triangle = [[]]
        for i in range(num_rows):
            for j in (range(i + 1)):
                if i in (0, 1) or j == 0 or i == j:
                    pascal_triangle[i].append(1)
                else:
                    pascal_triangle[i].append(pascal_triangle[i - 1][j - 1] + pascal_triangle[i - 1][j])
            pascal_triangle.append([])
        pascal_triangle.pop(-1)
        return pascal_triangle


solution = Solution()
print(solution.generate(5))