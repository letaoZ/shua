'''
45. Jump Game II
Medium

6456

248

Add to List

Share
Given an array of non-negative integers nums, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

You can assume that you can always reach the last index.

 

Example 1:

Input: nums = [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: nums = [2,3,0,1,4]
Output: 2
 

Constraints:

1 <= nums.length <= 104
0 <= nums[i] <= 1000
'''


class Solution:
    def jump0(self, nums: List[int]) -> int:
        
        ## dp[k] if we want to reach the index k of nums ( k is from 0 to len(nums)-1 ), min num of steps
        ## brutal
        N = len(nums)
        
        dp = [float('inf')]*N
        dp[0] = 0
        
        for i, k in enumerate(nums):
            if dp[i] == float('inf'):
                continue
            for ik in range(1,k+1):
                if i+ik >= N:
                    break
                dp[i+ik] = min(dp[i+ik], dp[i]+1)
        return dp[-1]
    
    def jump1(self, nums: List[int]) -> int:
        
        ## dp[k] if we want to reach the index k of nums ( k is from 0 to len(nums)-1 ), min num of steps
        ## brutal
        N = len(nums)
        
        dp = [float('inf')]*N
        dp[0] = 0
        
        for i, k in enumerate(nums):
            if dp[i] == float('inf'):
                continue
            for ik in range(k,0,-1):
                if i+ik >= N:
                    continue
                dp[i+ik] = min(dp[i+ik], dp[i]+1)
        return dp[-1]
    def jump(self, nums):
        ## greedy: we don't need to get all possible results, BUT just the best result
        N = len(nums)
        farthest = 0
        ending = 0
        res = 0
        for i in range(N-1):
            farthest = max(farthest, i + nums[i]) 
            if ending == i: ## use steps to reach farthest
                res += 1
                ending = farthest
        return res
        