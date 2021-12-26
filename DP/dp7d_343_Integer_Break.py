'''
343. Integer Break
Medium

2326

304

Add to List

Share
Given an integer n, break it into the sum of k positive integers, where k >= 2, and maximize the product of those integers.

Return the maximum product you can get.

 

Example 1:

Input: n = 2
Output: 1
Explanation: 2 = 1 + 1, 1 × 1 = 1.
Example 2:

Input: n = 10
Output: 36
Explanation: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36.
 

Constraints:

2 <= n <= 58
'''

class Solution:
    def integerBreak_bottomUP(self, n: int) -> int:
        if n <= 2:
            return 1
        
        res = 1
        dp = [0]*(n+1)
        dp[1] = 1
        dp[2] = 2
        
        ## time = O(num)
        def max_prod(num):
            if dp[num] > 0:
                return dp[num]
            res = num
            for i in range(1,num//2+1):
                res = max(res, max_prod(i)*max_prod(num-i))
                
            dp[num] = res
            return res
        
        
        ## time:= sum (O(num) ), num = 1,...n --> O(n**2)
        for i in range(1,n//2+1):
            res = max(res, max_prod(i)*max_prod(n-i))
            
        return res

    def integerBreak(self, n: int) -> int:
        if n<=2:
            return 1
        
        ##dp[k] max prod you get if sum = k
        ## dp[k] = max(dp[k-i]*dp[i]) for i in range(1,k//2 + 1)
        dp = [0 for k in range(n+1)]
        dp[1] = dp[2] = 1
        
        for k in range(3, n +1):
            for i in range(1, k//2 + 1):
                dp[k] = max(dp[k],max(i,dp[i]) * max(k-i, dp[k-i]) )
        return dp[n]