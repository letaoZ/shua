'''
5. Longest Palindromic Substring

Manacher's Algo
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
    def longestPalindrome_Manacher(self, s: str) -> str:
        if len(s) <= 1: return s
        
        ## Manacher's algo
        ## adding pads
        pads = ["#"]*(2*len(s) + 1 + 2) ## extra padding at the beginning and end; easy for comparison later
        pads[0] = '%'
        pads[-1] = '$' ## extra padding at the beginning and end; easy for comparison later
        for i in range(len(s)):
            pads[2+2*i] = s[i]
            
        ## mushave parameters
        center = 0
        right = 0
        maxlen = [0]*len(pads)
        
        ## these two are just for this problems
        res = 0
        res_i = 0
        for i in range(1, len(pads)-1): ## skip padding at the beginning and end
            if center<=i<right:
                i_mirror = 2*center - i
                maxlen[i] = min(right-i, maxlen[i_mirror])
            ## expand at i
            
            while ( pads[i + maxlen[i]+1] == pads[i-maxlen[i]-1]):
                maxlen[i]+= 1
            
            if (i + maxlen[i] > right):
                center = i
                right = i + maxlen[i]
                
                
            ## these ops are just for this problems
            if res < maxlen[i]:
                res = max(res, maxlen[i])
                res_i = i
        res_s = "".join([c for c in pads[res_i - maxlen[res_i] : res_i + maxlen[res_i] + 1] if c!='#'])
        return res_s

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
                        