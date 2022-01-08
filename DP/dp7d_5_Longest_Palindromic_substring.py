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


    def longestPalindrome_slower(self, s: str) -> str:
        
        if len(s) <= 1:
            return s
        
        max_length = 1
        res = s[0]
        for mid in range(len(s)):
            
            ## odd length
            L = 1
            l, r = mid-1, mid+1
            while l>=0 and r <len(s):
                if s[l] == s[r]:
                    L += 2
                    l -= 1
                    r += 1
                else:
                    break
            if L>max_length:
                res = s[l+1:r]
                max_length = L
            
            if mid+1<len(s) and s[mid] == s[mid+1]:
                L = 2
                l, r = mid-1, mid+2
                while l>=0 and r <len(s):
                    if s[l] == s[r]:
                        L += 2
                        l -= 1
                        r += 1
                    else:
                        break
                if L>max_length:
                    res = s[l+1:r]
                    max_length = L
        return res
                        