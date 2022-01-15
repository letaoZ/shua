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
        if n == 2:
            return 1
        if n == 3:
            return 2
        
        ## NOTE: if a factor f>=4, f =2+(f-2)--> 2*(f-2) >= f --> factor should only be 2 or 3
        ## every number n = 6x+b; since 6 = 3+3 or 2+2+2 --> so it should be written as 3+3
        ## b = 1, 2,3, good; b = 4 --> 2+2; (special cases); b = 5 ->2+3; 
        product = 1
        while(n>4):
            product*=3;
            n-=3;
        
        product*=n;
        return product
    
    def integerBreak_topdown(self, n: int) -> int:
        if n <= 2:
            return 1
        
        res = 1
        dp = [0]*(n+1)
        ## NOTE: here we assume dp[2] = 2 as we will NOTE run into case where n=2
        ## time = O(num)
        def max_prod(num):
            if dp[num] > 0:
                return dp[num]
            
            dp[num] = num
            res = num
            for i in range(1,num//2+1):
                res = max(res, max_prod(i)*max_prod(num-i))
                
            dp[num] = res
            return res
        
        
        ## time:= sum (O(num) ), num = 1,...n --> O(n**2)
        for i in range(1,n//2+1):
            res = max(res, max_prod(i)*max_prod(n-i))
            
        return res

    def integerBreak_bottomup(self, n: int) -> int:
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