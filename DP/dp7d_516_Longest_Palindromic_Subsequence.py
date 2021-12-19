'''
516. Longest Palindromic Subsequence
Medium

4389

237

Add to List

Share
Given a string s, find the longest palindromic subsequence's length in s.

A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.

 

Example 1:

Input: s = "bbbab"
Output: 4
Explanation: One possible longest palindromic subsequence is "bbbb".
Example 2:

Input: s = "cbbd"
Output: 2
Explanation: One possible longest palindromic subsequence is "bb".
 

Constraints:

1 <= s.length <= 1000
s consists only of lowercase English letters.
'''



class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        N = len(s)
        if N <= 1:
            return N
        
        
        
        ## dp[i][j] := max length palindromic subsequence in s[i...j]
        
        dp = [ [0]*N for _ in range(N) ]
        
        for i in range(N):
            dp[i][i] = 1
        
        ## induction on distance between i,j
        for l in range(1,N):
            for i in range(N-l):
                j = i+l
                
        
                dp[i][j] = max(dp[i+1][j-1] + 2*(s[i] == s[j]),
                              dp[i+1][j], dp[i][j-1])
        
        return dp[0][N-1]