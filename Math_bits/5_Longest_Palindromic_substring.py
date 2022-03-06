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
    def longestPalindrome(self, s: str) -> str:
        
        ## Manacher's algo
        ## adding pads
        
        pads = ['#'] * (2*len(s) + 1)
        for i in range(len(s)):
            pads[2*i + 1] = s[i]
        pads = ['^'] + pads + ['%'] ## added pading for easy of running comparison algo
        
        
        ## must have parameters
        maxLen = [0]*len(pads)
        center = 0
        rightmost = 0
        
        for i in range(2, len(pads) - 1):
            if i< center: ## about i's longest palindrome
                mirror_i = 2*center - i ## update i's current maxLen
                maxLen[i] = min(rightmost-i, maxLen[mirror_i])
                
            ## now see if we can expand beyond rightmorse
            ## we will stop because we added padding ^ and &
            while (pads[i+maxLen[i]+1] == pads[i-maxLen[i]-1]):
                maxLen[i] += 1
            
            if i+maxLen[i] > rightmost:
                rightmost = i+maxLen[i]
                center = i
        maxLen = maxLen[1:-1] ## remove the padding at the begnning and end
        len_res = max(maxLen)
        idx = maxLen.index(len_res)
       
        orig_left, orig_right = ((idx - len_res + 1) - 1 ) //2, ((idx + len_res - 1) - 1) // 2
        
        
        ## num of palindrome
        res = 0
        pads = pads[1:-1]
        for idx, v in enumerate(maxLen):
            if v > 0:
                if pads[idx] == "#":
                    res += v//2
                else:
                    res += (v-1) // 2
        print(res)
        
        
        
        return s[orig_left:orig_right+1]

class Solution1:
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
                        