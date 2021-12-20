'''
392. Is Subsequence
Easy

3420

261

Add to List

Share
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

 

Example 1:

Input: s = "abc", t = "ahbgdc"
Output: true
Example 2:

Input: s = "axc", t = "ahbgdc"
Output: false
 

Constraints:

0 <= s.length <= 100
0 <= t.length <= 104
s and t consist only of lowercase English letters.
 

Follow up: Suppose there are lots of incoming s, say s1, s2, ..., sk where k >= 109, and you want to check one by one to see if t has its subsequence. In this scenario, how would you change your code?
'''

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        @lru_cache(maxsize=1024)
        def searching(ss,tt):
            # print(f'searching: {ss} {tt}',)
            if ss in tt:
                ## this includes the case where ss==''
                return True
            
            if len(tt) == 0 or len(ss)>len(tt):
                return False
            i = 0
            
            for j in range(len(tt)):
                if len(ss[i:])>len(tt[j:]):
                    break
                elif ss[i] == tt[j]:
                    res = searching(ss[i+1:],tt[j+1:])
                    if res:
                        return res
                   
                        
            return False
        
        
        ## quick check
        if len(s)>len(t):
            return False
        
        set_s = set(s)
        set_t = set(t)
        if not set_s.issubset(set_t):
            return False
        ## time complexity
        ## len(s)*len(t)
        return searching(s,t)
            