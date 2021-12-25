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
    def integerBreak(self, n: int) -> int:
        if n <= 2:
            return 1
        
        res = 1
        dp = [0]*(n+1)
        dp[1] = 1
        dp[2] = 2
        
        def max_prod(num):
            if dp[num] > 0:
                return dp[num]
            res = num
            for i in range(1,num//2+1):
                res = max(res, max_prod(i)*max_prod(num-i))
                
            dp[num] = res
            return res
        
        for i in range(1,n//2+1):
            res = max(res, max_prod(i)*max_prod(n-i))
            
        return res