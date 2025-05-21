"""
73. Set Matrix Zeros

Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

You must do it in place.


Example 1:


Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]

Example 2:


Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]

Constraints:

m == matrix.length
n == matrix[0].length
1 <= m, n <= 200
-231 <= matrix[i][j] <= 231 - 1
 
"""

class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.]

        O (m + n) solution
        """
        m = len(matrix)
        n = len(matrix[0])


        columns = set()  # create two arrays columns and rows.  These arrays will hold information on which rows and columns are to be zeroed out.
        rows = set()    # using set will automatically remove any duplicates

        # first pass - find all zeros in the first matrix
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    columns.add(j)
                    rows.add(i)

        # second pass - zero out rows and columns

        for i in range(m):
            for j in range(n):
                if i in rows or j in columns:
                    matrix[i][j] = 0
        
        




s = Solution

matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
s.setZeroes(s, matrix)

print(matrix)