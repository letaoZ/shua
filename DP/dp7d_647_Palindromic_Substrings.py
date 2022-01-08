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