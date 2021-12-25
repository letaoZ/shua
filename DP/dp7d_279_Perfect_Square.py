'''
279. Perfect Squares
Medium

5973

272

Add to List

Share
Given an integer n, return the least number of perfect square numbers that sum to n.

A perfect square is an integer that is the square of an integer; in other words, it is the product of some integer with itself. For example, 1, 4, 9, and 16 are perfect squares while 3 and 11 are not.

 

Example 1:

Input: n = 12
Output: 3
Explanation: 12 = 4 + 4 + 4.
Example 2:

Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.
 

Constraints:

1 <= n <= 104
'''

class Solution:
    def numSquares(self, n: int) -> int:
        ## n is sum of 1, so it is at most "n"
        
        ## dp[k] := min num of sum of perfect squares
        
        dp = [k for k in range(0,n+1)]
        sq = [k**2 for k in range(int(n**0.5)+1)]
        
        for k in range(2,n+1):
            for sqn in sq:
                if k<sqn: break
                dp[k] = min(dp[k], dp[k-sqn] + 1)
        return dp[-1]