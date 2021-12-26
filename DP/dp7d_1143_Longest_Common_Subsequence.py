'''
1143. Longest Common Subsequence
Medium

5105

59

Add to List

Share
Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

For example, "ace" is a subsequence of "abcde".
A common subsequence of two strings is a subsequence that is common to both strings.

 

Example 1:

Input: text1 = "abcde", text2 = "ace" 
Output: 3  
Explanation: The longest common subsequence is "ace" and its length is 3.
Example 2:

Input: text1 = "abc", text2 = "abc"
Output: 3
Explanation: The longest common subsequence is "abc" and its length is 3.
Example 3:

Input: text1 = "abc", text2 = "def"
Output: 0
Explanation: There is no such common subsequence, so the result is 0.
'''

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        sz1, sz2 = len(text1),len(text2)
        if text1 in text2 or text2 in text1:
            return min(sz1,sz2)
        
        if len( set(text1).intersection(set(text2)) ) ==0:
            return 0
        a,b = text1,text2 ## easy to type
        
        ## dp[i][j] longest common subseq for a[:i] and b[:j]
        dp = [[0]*(1+sz2) for _ in range(1+sz1)]
        
        for i in range(1,sz1+1):
            for j in range(1,sz2+1):
                dp[i][j] = max(dp[i][j-1],dp[i-1][j],dp[i-1][j-1])
                if a[i-1] == b[j-1]:
                    dp[i][j] = max(1+dp[i-1][j-1],dp[i][j])
                    
                    
        return dp[sz1][sz2]