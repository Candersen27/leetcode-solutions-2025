"""
2901. Longest Unequal Adjacent Groups Subsequence II

You are given a string array words, and an array groups, both arrays having length n.

The hamming distance between two strings of equal length is the number of positions at which the corresponding characters are different.

You need to select the longest subsequence from an array of indices [0, 1, ..., n - 1], such that for the subsequence denoted as [i0, i1, ..., ik-1] having length k, the following holds:
    
    * For adjacent indices in the subsequence, their corresponding groups are unequal, i.e., groups[ij] != groups[ij+1], for each j where 0 < j + 1 < k.

    * words[ij] and words[ij+1] are equal in length, and the hamming distance between them is 1, where 0 < j + 1 < k, for all indices in the subsequence.

Return a string array containing the words corresponding to the indices (in order) in the selected subsequence. If there are multiple answers, return any of them.

Note: strings in words may be unequal in length.

Constraints:

* 1 <= n == words.length == groups.length <= 1000
* 1 <= words[i].length <= 10
* 1 <= groups[i] <= n
* words consists of distinct strings.
* words[i] consists of lowercase English letters.


Example 1:

Input: words = ["bab","dab","cab"], groups = [1,2,2]

Output: ["bab","cab"]

Explanation: A subsequence that can be selected is [0,2].

    - groups[0] != groups[2]
    - words[0].length == words[2].length, and the hamming distance between them is 1.

So, a valid answer is [words[0],words[2]] = ["bab","cab"].
Another subsequence that can be selected is [0,1].

    - groups[0] != groups[1]
    - words[0].length == words[1].length, and the hamming distance between them is 1.
So, another valid answer is [words[0],words[1]] = ["bab","dab"].
It can be shown that the length of the longest subsequence of indices that satisfies the conditions is 2.

"""




class Solution:
    def getWordsInLongestSubsequence(self, words: list[str], groups: list[int]) -> list[str]:
        
        def check_link(word_a, word_b, group_a, group_b):
            
            group_check = group_a != group_b
            length_check = len(word_a) == len(word_b)

            if group_check and length_check:
                hamming = 0
                for i in range(len(word_a)):
                    if word_a[i] != word_b[i]:
                        hamming += 1
            
                if hamming == 1:
                    return True
            
            
            return False
        

        def find_longest_substring():
            n = len(words)
            dp = [1] * n  # create a list of ones of size n.  This will keep track of the size of thelongest substring available ending at index i.

            for i in range(n):
                for j in range(i):
                    if check_link(words[j], words[i], groups[j], groups[i]):
                        dp[i] = max(dp[i], dp[j] + 1)

            longest_length =  max(dp)

            for i in range(len(dp)):
                if dp[i] == longest_length:
                    return i, dp
        
        # Main function Logic
        
        ending_index, dp = find_longest_substring()
        current_index = ending_index
        answer = []

        while current_index is not None:
            # Add current word to the front of answer
            answer.insert(0, words[current_index])

            # Find the previous index in the optimal path
            previous_index = None

            # Look backwards through all previous indices
            for j in range(current_index):
                # check if this j could be the previous step
                if (dp[j] == dp[current_index] - 1 and 
                check_link(words[j], words[current_index], groups[j], groups[current_index])):
                    previous_index = j
                    break
                
            current_index = previous_index

        return answer
    
words1 = ["cat", "bat", "bot", "blx", "fox", "fix"]
groups1 = [1,    2,    1,    2,    1,    2]

s = Solution()

temp = s.getWordsInLongestSubsequence(words1, groups1)

print(temp)