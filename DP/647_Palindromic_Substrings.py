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
        sz = len(s) 
        if sz <= 1: return 1
        if len(set(s)) == 1:
            return (sz * (sz+1))//2
            
            
        ## Manacher's algo
        cnt = 0
        ## padding
        ## abc --> $#a#b#c#% 
        pads = ["#"]*(2*len(s)+1 + 2)
        pads[0] = "$"
        pads[-1] = "%"
        
        for i in range(len(s)):
            pads[2+2*i] = s[i]
        
        ##manacher's
        
        center = 0 ## current center of a long palin
        right = 0  ## rightmost point of a palin
        maxlen = [0]*len(pads) ## maxLen[i] := max symmetry armlen about pads[i] (not including i); $#a#a#% -> at maxlen[1]: 1; maxlen[2]:2
        for i in range(1, len(pads)-1):
            if (center<=i<right):
                i_mirror = 2*center - i
                maxlen[i] = min(right-i, maxlen[i_mirror])
            ## expand center at i
            while( pads[i+maxlen[i] +1 ] == pads[i- maxlen[i] - 1 ]):
                maxlen[i] += 1
                
            ## if we have new center
            if (maxlen[i] +i > right):
                center = i
                right = maxlen[i] +i
                
            ## original s: will have a palin of len maxlen[i] 
            cnt += (maxlen[i] //2)
            
        cnt += sz ## individual letters
        
        return cnt
            
    def countSubstrings_BRUTAL(self, s: str) -> int:
        ## BRUTAL
        res = 1
        sz = len(s)
        if len(set(s)) == 1:
            return (sz*(sz+1)) // 2
        ## i is center
        for i in range(1,sz):
            ## odd
            cnt = 1 ## each letter is counted here
            l, r = i-1, i+1
            while (0<=l and r<sz and s[l] == s[r]):
                l -= 1
                r += 1
                cnt += 1
            res += cnt
            
            if ( s[i-1] == s[i]):
                cnt = 1 #
                l, r = i-2, i+1
                while (0<=l and r<sz and s[l] == s[r]):
                    l -= 1
                    r += 1
                    cnt += 1
                res += cnt
                
        return res