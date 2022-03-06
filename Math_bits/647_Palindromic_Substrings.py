'''
647. Palindromic Substrings
Medium

5590

149

Add to List

Share
Given a string s, return the number of palindromic substrings in it.

A string is a palindrome when it reads the same backward as forward.

A substring is a contiguous sequence of characters within the string.

 

Example 1:

Input: s = "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".
Example 2:

Input: s = "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
 

Constraints:

1 <= s.length <= 1000
s consists of lowercase English letters.
'''
class Solution:
    def countSubstrings(self, s: str) -> int:
        ## Manacher's
        pads = ['#']*(len(s)*2 + 1 + 2) ## add padding for begnning and end
        for i in range(len(s)):
            pads[i*2 + 2] = s[i]
        pads[0] = "^"
        pads[-1] = "%"
        ## must haves
        maxLen = [0]*len(pads)
        center = 0
        rightmost = 0
        
        for i in range(2,len(pads)-1):
            if i<center:
                i_mirror = 2*center - i ## my max arm length is at least the mirror's length; or the furthest I can reach before rightmost
                maxLen[i] = min(maxLen[i_mirror], rightmost - i)
            while ( pads[i-maxLen[i]-1] == pads[i+maxLen[i]+1]):
                maxLen[i] += 1 ## try extend the uncompared arms
            
            if i + maxLen[i] > rightmost:
                rightmost = i + maxLen[i]
                center = i
        ## remove bounds padding
        pads = pads[1:-1]
        maxLen = maxLen[1:-1]
        
        ## get all palin (center taken from pads) with length at most L
        ## NOTE: if center is even, then it's a letter in pads, else it's a "#"
        ## but we can always get corresponding bounds
        ## function to get all palindrom
        get_all_pal = False
        def get_palin(center,L, s):
            orig_left, orig_right = ( (center - L +1) - 1 )//2, ( (center + L -1) - 1 )//2
            res = []
            while orig_left <= orig_right:
                res.append(s[orig_left:orig_right+1])
                orig_left += 1
                orig_right -= 1
            return res
        
        if get_all_pal == True:
            res = []
            for center, L in enumerate(maxLen):
                if L == 0: 
                    continue

                res.extend(get_palin(center,L,s))

        ## get number of palin
        res = len(s)
        ## now count the palin of len > 1
        for i,v in enumerate(maxLen):
            ## if ith position if '#' i.e. i is even
            if i == 0:
                continue
            res += (v//2)
        return res
        
class Solution:
    def countSubstrings(self, s: str) -> int:
        ## brutal
        res = 0
        for mid in range(len(s)):
            ## odd length
            cnt = 1
            l, r = mid-1, mid+1
            while l>=0 and r<len(s):
                if s[l] == s[r]:
                    cnt += 1
                    l -= 1
                    r += 1
                else:
                    break
            res += cnt
            
            if mid+1<len(s) and s[mid] == s[mid+1]:
                cnt = 1
                l = mid-1
                r = mid+2
                while l>=0 and r<len(s):
                    if s[l] == s[r]:
                        cnt += 1
                        l -= 1
                        r += 1
                    else:
                        break
                        
                        
                res += cnt
                
                
        return res