'''5. Longest Palindromic Substring
Medium

14785

864

Add to List

Share
Given a string s, return the longest palindromic substring in s.

 

Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"
 

Constraints:

1 <= s.length <= 1000
s consist of only digits and English letters.
'''

class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        ## brutal
        N = len(s)
        if N <= 1:
            return s
        res = s[0]
        res_l = 1
        for i in range(N):
            for j in range(i+res_l+1,N+1):
                if s[i:j] == s[i:j][::-1]:
                    res = s[i:j]
                    res_l = len(res)
            if res_l == N:
                return res
        return res