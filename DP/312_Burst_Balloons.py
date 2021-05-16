'''
312. Burst Balloons
Hard

You are given n balloons, indexed from 0 to n - 1. 
Each balloon is painted with a number on it represented by an array nums. You are asked to burst all the balloons.

If you burst the ith balloon, you will get nums[i - 1] * nums[i] * nums[i + 1] coins. 
If i - 1 or i + 1 goes out of bounds of the array, then treat it as if there is a balloon with a 1 painted on it.

Return the maximum coins you can collect by bursting the balloons wisely.

 

Example 1:

Input: nums = [3,1,5,8]
Output: 167
Explanation:
nums = [3,1,5,8] --> [3,5,8] --> [3,8] --> [8] --> []
coins =  3*1*5    +   3*5*8   +  1*3*8  + 1*8*1 = 167
Example 2:

Input: nums = [1,5]
Output: 10
 

Constraints:

n == nums.length
1 <= n <= 500
0 <= nums[i] <= 100
'''

class Solution:
    def maxCoins_dp_mem_slow(self, nums: List[int]) -> int:

        
        ## if just one number, take its power
        num_st = set(nums)
        if len(num_st) ==1:
            if len(nums)>3:
                return nums[0]**3*(len(nums) -2 ) + nums[0]**2 +nums[0]

            
        sz = len(nums)
        if sz == 0:
            return 0
        if sz == 1:
            return nums[0]
        
        
        ## pop all zeros
        i0 = 0
        i = 0
        while i<sz:
            if nums[i] != 0:
                nums[i0] = nums[i]
                i += 1
                i0 += 1
            else:
                i += 1
        nums = nums[:i0]
        sz = len(nums)
        if sz == 0:
            return 0
        if sz == 1:
            return nums[0]        
        
        def prod(i,j,k,nums):
            p1=p2=p3 = 1

            if i>=0 and i<len(nums):
                p1 = nums[i]
            if j>=0 and j<len(nums):
                p2 = nums[j]
            if k>=0 and k<len(nums):
                p3 = nums[k]
            return p1*p2*p3

        def searching(nums,dp):
            if not nums:
                return 0
            res = 0
            tag = '_'.join([str(n) for n in nums])
            if tag in dp:
                return dp[tag]

            for i in range(len(nums)):
                P = prod(i-1,i,i+1,nums)
                res = max(res, P+ searching(nums[:i]+nums[i+1:], dp))
            dp[tag] = res

            return res
        
        dp = {}
        res = searching(nums, dp)
        return res
    
    ## reason for barely working is because
    ## input could be one number repeat n times...
    def maxCoins_barely_working(self, nums: List[int]) -> int:
        ## if just one number, take its power
        num_st = set(nums)
        if len(num_st) ==1:
            if len(nums)>3:
                return nums[0]**3*(len(nums) -2 ) + nums[0]**2 +nums[0]
        
        ## dp[i][j]: max coins you can get out of of nums[i] to nums[j]
        sz = len(nums)
        if sz == 0:
            return 0
        if sz == 1:
            return nums[0]
        
        
        ## pop all zeros
        i0 = 0
        i = 0
        while i<sz:
            if nums[i] != 0:
                nums[i0] = nums[i]
                i += 1
                i0 += 1
            else:
                i += 1
        nums = nums[:i0]
        sz = len(nums)
        if sz == 0:
            return 0
        if sz == 1:
            return nums[0]        
        
        ## starting DP
        dp = [ [0]*(sz+ 2) for _ in range(sz+2)]  
        
        ## add cushion
        nums = [1] + nums + [1]
        for L in range(0,sz):

            for i in range(1,sz+1-L):
                j = i+L
                for k in range(i,j+1):
                    ## if k is not exploded and it is the last to be exploded
                    dp[i][j] = max(dp[i][j], dp[i][k-1] + nums[k]*nums[i-1]*nums[j+1]+dp[k+1][j])
        return dp[1][sz]
    
    def maxCoins_bottomUp(self, nums: List[int]) -> int:
        ## if just one number, take its power
        num_st = set(nums)
        if len(num_st) ==1:
            if len(nums)>3:
                return nums[0]**3*(len(nums) -2 ) + nums[0]**2 +nums[0]
        

        ## huahua method,
        ## pop all zeros
        sz = len(nums)
        i0 = 0
        i = 0
        while i<sz:
            if nums[i] != 0:
                nums[i0] = nums[i]
                i += 1
                i0 += 1
            else:
                i += 1
        nums = nums[:i0]
        sz = len(nums)
        if sz == 0:
            return 0
        if sz == 1:
            return nums[0]  
        
        
        
        # reframe the problem
        nums = [1] + nums + [1]

        # cache this
        @lru_cache(None)
        def dp(left, right):

            # no more balloons can be added
            if left + 1 == right: return 0

            # add each balloon on the interval and return the maximum score
            return max(nums[left] * nums[i] * nums[right] + dp(left, i) + dp(i, right) for i in range(left+1, right))

        # find the maximum number of coins obtained from adding all balloons from (0, len(nums) - 1)
        return dp(0, len(nums)-1)