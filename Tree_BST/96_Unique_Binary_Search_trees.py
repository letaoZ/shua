'''
96. Unique Binary Search Trees
Medium

6344

248

Add to List

Share
Given an integer n, return the number of structurally unique BST's (binary search trees) which has exactly n nodes of unique values from 1 to n.

 

Example 1:


Input: n = 3
Output: 5
Example 2:

Input: n = 1
Output: 1
 

Constraints:

1 <= n <= 19
'''
class Solution:
    def numTrees(self, n: int) -> int:
        
        
        if n<=1:
            return n
        
        dp = [[0]*(n+1) for _ in range(n+1)]
        def searching(lo,hi):
            
            if lo > hi:
                ## when lo==hi, we get 1; consider using lo or hi as root as well
                return 1
            if dp[lo][hi]:
                return dp[lo][hi]
            res = 0
            for rt in range(lo,hi+1):
                ln = searching(lo,rt-1)
                rn = searching(rt+1,hi)
                res += ln*rn
            dp[lo][hi] = res
            return res
        
        return searching(1,n)