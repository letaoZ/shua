'''
10. Regular Expression Matching
Hard

7357

1020

Add to List

Share
Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*' where:

'.' Matches any single character.​​​​
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).

 

Example 1:

Input: s = "aa", p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
Example 2:

Input: s = "aa", p = "a*"
Output: true
Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".
Example 3:

Input: s = "ab", p = ".*"
Output: true
Explanation: ".*" means "zero or more (*) of any character (.)".
 

Constraints:

1 <= s.length <= 20
1 <= p.length <= 30
s contains only lowercase English letters.
p contains only lowercase English letters, '.', and '*'.
It is guaranteed for each appearance of the character '*', there will be a previous valid character to match.


'''
class Solution:
    def isMatch_dfs_no_memo(self, s: str, p: str) -> bool:
        
        s = list(s)
        while '**' in p:
            p = p.replace('**','*')
        p = list(p)
        
        i_s, i_p = 0, 0
        Ns, Np = len(s), len(p)       
        
        def dfs(i_s, i_p):
            if i_s >= Ns and i_p >= Np:
                return True
            elif i_s >= Ns:
                if p[i_p] == "*":
                    return dfs(i_s, i_p+1)
                elif (i_p + 1 < Np and p[i_p + 1] == '*'):
                    return dfs(i_s, i_p + 2)
                else:
                    return False
            elif i_p >= Np:
                return False
            
            elif s[i_s] == p[i_p] or p[i_p] == '.':
                if i_p + 1 < Np and p[i_p + 1] == '*':
                    return ( dfs(i_s, i_p+2) ## match zero times
                            or dfs(i_s+1, i_p) ) ## match one time, so we keep p the same, see if to match one more time or move on
                else:
                    return dfs(i_s + 1, i_p + 1)
            else:
                if i_p + 1 < Np and p[i_p + 1] == '*':
                    return dfs(i_s, i_p+2) ## match zero times
                else:
                    return False
                
        res = dfs(0,0)
        return res
    
    def isMatch(self, s: str, p: str) -> bool:
        ## use DFS + memorize states
        ## dfs: v = s[:i], p[:j] = len(s)+len(p);
        ##      e = (s[:i], p[:j]) = len(s)*len(p)
        ## so time = O(len(s)*len(p))
        
        s = list(s)
        while '**' in p:
            p = p.replace('**','*')
        p = list(p)
        
        i_s, i_p = 0, 0
        Ns, Np = len(s), len(p)       
        
        memo = dict()
        def dfs(i_s, i_p):
            if (i_s, i_p) in memo:
                return memo[(i_s, i_p)]
            
            res = False
            if i_s >= Ns and i_p >= Np:
                res = True
            elif i_s >= Ns:
                if p[i_p] == "*":
                    res = dfs(i_s, i_p+1)
                elif (i_p + 1 < Np and p[i_p + 1] == '*'):
                    res = dfs(i_s, i_p + 2)
                else:
                    res = False
            elif i_p >= Np:
                res = False
            
            elif s[i_s] == p[i_p] or p[i_p] == '.':
                if i_p + 1 < Np and p[i_p + 1] == '*':
                    res = ( dfs(i_s, i_p+2) ## match zero times
                            or dfs(i_s+1, i_p) ) ## match one time, so we keep p the same, see if to match one more time or move on
                else:
                    res = dfs(i_s + 1, i_p + 1)
            else:
                if i_p + 1 < Np and p[i_p + 1] == '*':
                    res = dfs(i_s, i_p+2) ## match zero times
                else:
                    res = False
            memo[(i_s, i_p)] = res
            return res
                
        res = dfs(0,0)
        return res
