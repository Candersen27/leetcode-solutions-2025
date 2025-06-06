"""
96. Unique Binary Search Trees
Given an integer n, return the number of structurally unique BST's (binary search trees) which has exactly n nodes of unique values from 1 to n.

 

Example 1:


Input: n = 3
Output: 5
Example 2:

Input: n = 1
Output: 1
 

Constraints:

1 <= n <= 19
"""

class Solution:
    def numTrees(self, n: int) -> int:
        
        
        def getCatalan(n: int, catalan_dict) -> dict:

            if n in catalan_dict:
                return catalan_dict
            
            if n-1 not in catalan_dict:
                catalan_dict = getCatalan(n-1, catalan_dict)
                

            catalan_num = 0

            for i in range(1, n+1):
                left = catalan_dict[i-1]
                right = catalan_dict[n-i]
                catalan_num += left * right

            catalan_dict[n] = catalan_num

            return catalan_dict

        catalan_dict = {0:1, 1:1, 2:2, 3:5}

        catalan_dict = getCatalan(n, catalan_dict)

        return catalan_dict[n]
    


s = Solution

print(s.numTrees(s, 17))