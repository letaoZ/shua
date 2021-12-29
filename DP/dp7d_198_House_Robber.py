'''
198. House Robber    
Medium

9880

228

Add to List

Share
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

 

Example 1:

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.
'''
class Solution:
    def rob0(self, nums: List[int]) -> int:
        ## dp[k] max amount of money you can get if there are k houses
        ## dp[k] =max( max(dp[:k]), max(dp[:k-1]) + nums[k] ) := either rob the kth house or not
        N = len(nums)
        dp = [0]*(N)
        dp[0] = nums[0]
        
        ## use a tmp variable to keep track of 2 steps before: max dp
        tmp_max = 0
        for i in range(1,N):
            # dp[i] = max( max(dp[:i]), max(dp[:i-1]) + nums[i] )
            tmp_max1 = max(tmp_max, dp[i-1])
            dp[i] = max( max(tmp_max, dp[i-1]), tmp_max + nums[i] )
            tmp_max = tmp_max1
            
        return dp[-1]            
    def rob(self, nums: List[int]) -> int:
        ## dp[k] max amount of money you can get if there are k houses
        ## dp[k] =max( max(dp[:k]), max(dp[:k-1]) + nums[k] ) := either rob the kth house or not
        N = len(nums)
        if N<=1:
            return max(nums)

        dp = [0]*(N)
        dp[0] = nums[0]
        
        ## use a tmp variable to keep track of 2 steps before: max dp
        for i in range(1,N):
            dp[i] = max(dp[i-2] + nums[i], dp[i-1])
            
        return dp[-1]            
    
    def rob_const_mem(self, nums: List[int]) -> int:
        
        
        if len(nums) <= 2:
            return max(nums)
        
        ## max you get rob 2 house ago, max you get rob 1 house ago
        d0, d1 = nums[0], max(nums[0], nums[1])
        ## dp[k] = max(dp[k-1], dp[k-2] + nums[k]), max you get robbing first k houses 
        
        res = d0
        for k in range(2,len(nums)):
            dtmp = max(d1, d0+nums[k])
            res = max(res, dtmp)
            d0, d1 = d1, dtmp
            print(d0,d1)

        return res