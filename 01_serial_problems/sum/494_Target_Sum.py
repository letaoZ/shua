'''
494. Target Sum
Medium

You are given an integer array nums and an integer target.

You want to build an expression out of nums by adding one of the symbols '+' and '-' before each integer in nums and then concatenate all the integers.

For example, if nums = [2, 1], you can add a '+' before 2 and a '-' before 1 and concatenate them to build the expression "+2-1".
Return the number of different expressions that you can build, which evaluates to target.

 

Example 1:

Input: nums = [1,1,1,1,1], target = 3
Output: 5
Explanation: There are 5 ways to assign symbols to make the sum of nums be target 3.
-1 + 1 + 1 + 1 + 1 = 3
+1 - 1 + 1 + 1 + 1 = 3
+1 + 1 - 1 + 1 + 1 = 3
+1 + 1 + 1 - 1 + 1 = 3
+1 + 1 + 1 + 1 - 1 = 3
Example 2:

Input: nums = [1], target = 1
Output: 1
 

Constraints:

1 <= nums.length <= 20
0 <= nums[i] <= 1000
0 <= sum(nums[i]) <= 1000
-1000 <= target <= 1000
'''


class Solution: 
    
    ## Transform to 0-1 knapsack
    def findTargetSumWays_knapsack(self, nums: List[int], target: int) -> int:

        
        ## idea: P-- sum of positive, N -- sum of negative
        ## P+N = total, P-N = target
        ## so 2P = tar+total --> P = (tar+total)/2 new target
        ## problem transform in to 01 knapsack
        
        total = sum(nums)
        P = (total+target)//2
        if 2* ( P )!=total+target:
            return 0
        if abs(target) > total:
            return 0
        
        
        ## mew target becomes P
        ## partial sum = P
        
        dp = [0 for _ in range(2*total + 1)]
        dp[0] = 1
        for n in nums:
            for ss in reversed(range(0, P-n +1 )):
                ## in knapsack, this is max(dp[weight], dp[weight-wi]+vi)

                dp[ss+n] += dp[ss]
        return dp[P]


    def findTargetSumWays_dp_2d(self, nums: List[int], S: int) -> int:
        total = sum(nums)
        cnt = 0
        if S>total or S<-total: return 0
        # if S in [total, -total]: return 1
        
        
        sz = len(nums)
        dp = [[0]*(2*total+1) for _ in range(sz + 1)]
        
                

        ## here: due to shift by negative total
        ## dp[0][total] means sum = 0
        dp[0][total] = 1
        for nn,num in enumerate(nums):
            for ss in range(num, 2*total+1-num):
                if dp[nn][ss]:
                    dp[nn+1][ss+num] += dp[nn][ss]
                    dp[nn+1][ss-num] += dp[nn][ss]
        return dp[-1][S+total]
        
            
    def findTargetSumWays_dp_reduce_space(self, nums: List[int], S: int) -> int:
         ## dp + reduce space
        total = sum(nums)
        cnt = 0
        if S>total or S<-total: return 0
        # if S in [total, -total]: return 1
        
        
        sz = len(nums)
        dp = [0]*(2*total+1) 
        
                

        ## here: due to shift by negative total
        ## dp[0][total] means sum = 0
        dp[total] = 1
        for nn,num in enumerate(nums):
            tmp = [0]*(2*total+1) 
            for ss in range(num, 2*total+1-num):
                if dp[ss]:
                    tmp[ss+num] += dp[ss]
                    tmp[ss-num] += dp[ss]
                    
            dp = tmp
        return dp[S+total]
        
            
