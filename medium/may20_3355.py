"""
3355. Zero Array Transformation I
Medium

You are given an integer array nums of length n and a 2D array queries, where queries[i] = [li, ri].

For each queries[i]:

Select a subset of indices within the range [li, ri] in nums.
Decrement the values at the selected indices by 1.
A Zero Array is an array where all elements are equal to 0.

Return true if it is possible to transform nums into a Zero Array after processing all the queries sequentially, otherwise return false.

 Example 1:

Input: nums = [1,0,1], queries = [[0,2]]

Output: true

Explanation:

For i = 0:
Select the subset of indices as [0, 2] and decrement the values at these indices by 1.
The array will become [0, 0, 0], which is a Zero Array.
Example 2:

Input: nums = [4,3,2,1], queries = [[1,3],[0,2]]

Output: false

Explanation:

For i = 0:
Select the subset of indices as [1, 2, 3] and decrement the values at these indices by 1.
The array will become [4, 2, 1, 0].
For i = 1:
Select the subset of indices as [0, 1, 2] and decrement the values at these indices by 1.
The array will become [3, 1, 0, 0], which is not a Zero Array.


Constraints:

1 <= nums.length <= 105
0 <= nums[i] <= 105
1 <= queries.length <= 105
queries[i].length == 2
0 <= li <= ri < nums.length 
"""


class Solution:
    def isZeroArray(self, nums: list[int], queries: list[list[int]]) -> bool:

        n = len(nums)
        count_array = [0] * n # initialize a count array with zeros, this will show how many times each value in nums will show up in the ranges from queries
        diff_array = [0] * (n + 1) # initialize a difference array that will be used to keep track of the collective ranges in queries (add an extra index to handle R+1 safely)


        for L, R in queries:
            diff_array[L] += 1 # increment the index of L in the difference array
            if R + 1 < n + 1:
                diff_array[R + 1] -= 1 # decrement the indext after R in the difference array

        count_array[0] = diff_array[0] # initialize the first element of count array.
        running_sum = 0
    
        for i in range(n):
            running_sum += diff_array[i]
            count_array[i] = running_sum
            if count_array[i] < nums[i]:
                return False
        
        return True
    





s = Solution
nums = [4,3,2,1] 
queries = [[1,3],[0,2]]
answer = s.isZeroArray(s, nums, queries)

print(answer)
        
nums2 = [3]
queries2 = [0,0], [0,0]
answer2 =  s.isZeroArray(s, nums2, queries2)
print(answer2)