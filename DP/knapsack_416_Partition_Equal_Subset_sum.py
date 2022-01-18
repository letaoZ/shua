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
    
    
    def canPartition(self, nums: List[int]) -> bool:
        target = sum(nums) // 2
        
        if target*2 != sum(nums):
            return False
        
        
        dp = [False]*(target+1)
        dp[0] = True
        
        for n in nums:
            for s in range(target,n-1,-1):
                dp[s] = (dp[s] or dp[s-n])
            if dp[target]:
                return True

        return False
                
    def canPartition(self, nums: List[int]) -> bool:
        target_sum = 0
        for kk in nums:
            target_sum += kk
        
        if target_sum%2!=0: 
            return False
        
        if target_sum//2 in nums:
            return True
        

        
        dp = [False]*(target_sum+1) 
        dp[0] = True
        
        for i in range(1,len(nums)+1):
            # for w in reversed(range(0,target_sum+1)):
            for w in range(target_sum,-1,-1):

                if dp[w]:
                    dp[w+nums[i-1]] = True
            if dp[target_sum//2]:
                return True
        return False
                
