"""
3337. Total characters in String after transformations 2

You are given a string s consisting of lowercase English letters, an integer t representing the number of transformations to perform, and an array nums of size 26. In one transformation, every character in s is replaced according to the following rules:

* Replace s[i] with the next nums[s[i] - 'a'] consecutive characters in the alphabet. For example, if s[i] = 'a' and nums[0] = 3, the character 'a' transforms into the next 3 consecutive characters ahead of it, which results in "bcd".

* The transformation wraps around the alphabet if it exceeds 'z'. For example, if s[i] = 'y' and nums[24] = 3, the character 'y' transforms into the next 3 consecutive characters ahead of it, which results in "zab".

Return the length of the resulting string after exactly t transformations.

Since the answer may be very large, return it modulo 10^9 + 7.
"""

"""
Example 1:

Input: s = "abcyy", t = 2, nums = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2]

Output: 7

Explanation:

First Transformation (t = 1):

'a' becomes 'b' as nums[0] == 1
'b' becomes 'c' as nums[1] == 1
'c' becomes 'd' as nums[2] == 1
'y' becomes 'z' as nums[24] == 1
'y' becomes 'z' as nums[24] == 1
String after the first transformation: "bcdzz"


Second Transformation (t = 2):

'b' becomes 'c' as nums[1] == 1
'c' becomes 'd' as nums[2] == 1
'd' becomes 'e' as nums[3] == 1
'z' becomes 'ab' as nums[25] == 2
'z' becomes 'ab' as nums[25] == 2
String after the second transformation: "cdeabab"
Final Length of the string: The string is "cdeabab", which has 7 characters.
"""

class Solution:
    def lengthAfterTransformations(self, s: str, t: int, nums: list[int]) -> int:
        MOD = 10**9 + 7

        def build_transformation_matrix(nums):
            matrix = [[0] * 26 for _ in range(26)] # initialize what will be the transformation matrix  (zeros for now)
            for i in range(26):
                num_chars = nums[i] # How many characters this transforms into

                for j in range(num_chars): # For each of those characters
                    target_pos = (i + 1 + j) % 26 # start with the next letter, and use mod to wrap around
                    matrix[i][target_pos] = 1

            return matrix

        def matrix_multiply(mat_1, mat_2):
            result = [[0] * 26 for _ in range(26)] 
            for i in range(26):
                for j in range(26):
                    for k in range(26):
                        result[i][j] = (result[i][j] + mat_1[i][k] * mat_2[k][j]) % MOD
            return result

        def matrix_power(mat, p):
            if p == 0: # Return identity matrix
                identity = [[0] * 26 for _ in range(26)]
                for i in range(26):
                    identity[i][i] = 1
                return identity

            if p == 1: 
                return mat
            
            if p % 2 == 0:
                # if the power is even, matrix^power = (matrix^(power/2))^2
                half_p = matrix_power(mat, p // 2)  # The Recursion here is what makes this algorithm optimal
                return matrix_multiply(half_p, half_p) # square the matrix
            
            else: # if the power is odd: matrix^power = matrix^(power-1) * matrix
                return matrix_multiply(matrix_power(mat, p - 1), mat) # Recursion here as well  
            

        # main logic

        # Step 1: build initial count vector
        letter_count = [0] * 26
        empty_letter_count = letter_count # copy count to use as a baseline for later
        
        alpha_num = {chr(i + 97): i for i in range(26)}  # create a dictionary using unicode characters a:0, b:1, ... z:25

        for letter in s:
            idx = alpha_num[letter]
            letter_count[idx] += 1
        
        # Step 2: Build Transformation Matrix
        trans_mat = build_transformation_matrix(nums)

        # Step 3: Comput trans_mat^t
        result_mat = matrix_power(trans_mat, t)

        # Step 4: apply the transformation to our count vector
        final_count = [0] * 26

        for j in range(26):
            for i in range(26):
                final_count[j] = (final_count[j] + letter_count[i] * result_mat[i][j]) % MOD
        
        # Step 5: Sum up the final counts
        return sum(final_count) % MOD


S = Solution()

num = S.lengthAfterTransformations(s = "abcyy", t = 2, nums = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2])
print(num)

num2 = S.lengthAfterTransformations(s = "azbk", t = 1, nums = [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2])
print(num2)

