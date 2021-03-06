'''
213. House Robber II
Medium

4246

74

Add to List

Share
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

 

Example 1:

Input: nums = [2,3,2]
Output: 3
Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent houses.
Example 2:

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.
Example 3:

Input: nums = [1,2,3]
Output: 3
 

Constraints:

1 <= nums.length <= 100
0 <= nums[i] <= 1000
'''

class Solution:
    def rob(self, nums: List[int]) -> int:
        ## use DP: there are two cases:
        ## if starts with rob nums[0], then cannot rob nums[-1]
        ## if starts with rob nums[1], then can rob nums[-1]
        
        N = len(nums)
        if N<=2:
            return max(nums)
        
        ## starts with rob nums[0]
        ## dp[k] := if there are totally k items, max you can get
        ## here we ignore nums[N-1]
        dp = [0]*(N+1)
        dp[1] = nums[0]
        for k in range(2,N):## we don't count the last house nums[N-1]
            dp[k] = max(dp[k-2]+nums[k-1], dp[k-1]) 
        res1 = dp[N-1]
        
        
        
        ## starts with rob nums[1]
        ## dp[k] := if there are totally k items, max you can get
        ## here we can count nums[N-1]
        dp = [0]*(N+1)
        dp[2] = nums[1] 
        for k in range(3,N+1):## we don't count the last house nums[N-1]
            dp[k] = max(dp[k-2]+nums[k-1], dp[k-1]) 
        res2 = dp[N]
        
        return max(res1, res2)


    def rob(self, nums: List[int]) -> int:
        ## consider run rob twice
        ## one starts with nums[0], then you can ONLY end with nums[-2]
        ## the other starts with nums[1], then you can end with nums[-1]
        
        ## two days ago, vs on day ago max
        if len(nums)<=3:
            return max(nums)
        
        
        dp0, dp1 = nums[0], max(nums[0:2])
        
        dp0, dp1 = dp1, max(dp0+nums[2], dp1)
        dpt0, dpt1 = nums[1], max(nums[1:3])
        res = max(dp1,dpt1)
        for n in range(3,len(nums)-1):
            dp_tmp = max(dp0+nums[n],dp1)
            dpt_tmp = max(dpt0+nums[n],dpt1)
            dp0, dp1 = dp1, dp_tmp
            dpt0, dpt1 = dpt1, dpt_tmp
            res = max(dp1,dpt1)

        dpt_tmp = max(dpt0+nums[-1],dpt1)
            
        res = max(res, dpt_tmp)            
        return res