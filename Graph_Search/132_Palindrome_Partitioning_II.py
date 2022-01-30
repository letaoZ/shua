'''
132. Palindrome Partitioning II
Hard

3032

75

Add to List

Share
Given a string s, partition s such that every substring of the partition is a palindrome.

Return the minimum cuts needed for a palindrome partitioning of s.

 

Example 1:

Input: s = "aab"
Output: 1
Explanation: The palindrome partitioning ["aa","b"] could be produced using 1 cut.
Example 2:

Input: s = "a"
Output: 0
Example 3:

Input: s = "ab"
Output: 1
 

Constraints:

1 <= s.length <= 2000
s consists of lowercase English letters only.
'''

## can be solved by backtracking, but tooooo slow!!
class Solution:
    def minCut_slow_use_backtracking(self, s: str) -> int:
        ## backtracking and count length as result
        ##N * 2^N!
        if len(set(s)) == 1:
            return 0
        
        pals = {}
        def isPal(s):
            if s in pals:
                return pals[s]
            
            l, r = 0, len(s) - 1
            while l<=r and s[l] == s[r]:
                l += 1
                r -= 1
                
            pals[s] = (l>r)
            return l>r
        
        
        ## keep track of number of parts
        ## result will be number of parts - 1
        res = len(s) ## for update in dfs
        npartitions = {"":0}
        
        def get_partitions(ss):
            if ss in pals:
                if pals[ss]:
                    return 1
            if ss in npartitions:
                return npartitions[ss]
            tt = ""
            res = float('inf')
            for i in range(len(ss)):
                tt += ss[i]
                
                if not isPal(tt):
                    continue
                res = min(res, 1+get_partitions(ss[i+1:]))
            
            npartitions[ss] = res
            return res
        res = get_partitions(s)
        return res-1
                    
            
    def minCut(self, s: str) -> int:
        
        ## dp[i][j] := if s[i...j] if palind
        N = len(s)
        dp = [[0]*(N) for _ in range(N)]
        for i in range(N):
            dp[i][i] = True
        
        ## NOTE: res[i] keeps track of min number of palin in s[..i], final cuts needs to subtract by 1
        res = [_ for _ in range(1, N+1)]    
        res.append(0)## cushion
        for i in range(1,N):
            for j in range(i+1):## important to go to j == i!
                if (s[j] == s[i]) and (j+1>i-1 or dp[j+1][i-1] ):
                    dp[j][i] = True
                    res[i] = min(res[i], 1+res[j-1])
        # print(res)
        return res[N-1] - 1
            
            