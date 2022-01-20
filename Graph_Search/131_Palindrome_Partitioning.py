'''
131. Palindrome Partitioning
Medium

5840

173

Add to List

Share
Given a string s, partition s such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of s.

A palindrome string is a string that reads the same backward as forward.

 

Example 1:

Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]
Example 2:

Input: s = "a"
Output: [["a"]]
 

Constraints:

1 <= s.length <= 16
s contains only lowercase English letters.
'''
class Solution:
    def partition_backtracking(self, s: str) -> List[List[str]]:
        ## time: N2^N , N = len(s), the N here is used for checking palidrome
        ## use tree structure to illustrate this
        res = set()
        
        candi = list(s)
        
        def if_pal(ss):
            l, r = 0, len(ss)-1
            while l<=r and ss[l] == ss[r]:
                l += 1
                r -= 1
            return l>r
                
        def dfs(i,candi,trace,):
            
            
            if i == len(s):
                l = sum(len(_) for _ in trace)
                if l == len(s):
                    res.add(tuple(trace))
            
            t = ""
            for j in range(i,len(candi)):
                t += candi[j]
                if not if_pal(t):
                    continue
                
                trace.append(t)
                dfs(j+1,candi,trace)
                trace.pop()
                
                
        dfs(0,candi,[])
        
        res = list(list(_) for _ in res)
        return res
    
    
    