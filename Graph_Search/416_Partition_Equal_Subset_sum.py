'''
416. Partition Equal Subset Sum

Given a non-empty array nums containing only positive integers, 
find if the array can be partitioned into two subsets 
such that the sum of elements in both subsets is equal. 

Example 1:

Input: nums = [1,5,11,5]
Output: true
Explanation: The array can be partitioned as [1, 5, 5] and [11].
Example 2:

Input: nums = [1,2,3,5]
Output: false
Explanation: The array cannot be partitioned into equal sum subsets.
 

Constraints:

1 <= nums.length <= 200
1 <= nums[i] <= 100


'''

class Solution:
    def canPartition_dp_2d(self, nums: List[int]) -> bool:
        target_sum = 0
        for kk in nums:
            target_sum += kk
        
        if target_sum%2!=0: 
            return False
        
        if target_sum//2 in nums:
            return True
        

        
        dp = [ [False]*(target_sum+1) for _ in range(len(nums)+1) ]
        dp[0][0] = True
        
        for i in range(1,len(nums)+1):
            for w in reversed(range(0,target_sum+1)):
                dp[i][w] |= dp[i-1][w]

                if dp[i][w]:
                    dp[i][w+nums[i-1]] = True
            if dp[i][target_sum//2]:
                return True
        return False
    
    def canPartition_knapsack(self, nums: List[int]) -> bool:
        ss = sum(nums)
        if ss & 1 == 1:
            return False
        
        target = ss//2
        
        
        dp = [False]*(target+1)
        dp[0] = True
        for candi in nums:
            for ss in range(target,candi-1,-1):
                dp[ss] |= dp[ss-candi]
                if dp[target]:
                    return True
        return dp[target]

    
    def canPartition_dfs(self, nums: List[int]) -> bool:
        target = sum(nums) // 2
        
        if target*2 != sum(nums):
            return False
        visited = set()
        ## is something is in visited, means it cannot be reached
        ## if it can be reached, then we have already returned True
        def dfs(nums, target):
            if target < 0:
                return False
            if target == 0:
                return True
            if target in visited:
                return False
            visited.add(target)
            for k,n in enumerate(nums):
                if dfs(nums[k+1:],target-n):
                    return True
            return False
        
        return dfs(nums,target)