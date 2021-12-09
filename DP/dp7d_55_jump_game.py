'''
55. Jump Game
Medium

8956

526

Add to List

Share
You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.

 

Example 1:

Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.
 

Constraints:

1 <= nums.length <= 104
0 <= nums[i] <= 105
'''

class Solution:
    def canJump0(self, nums: List[int]) -> bool:
        ## index k can be reached if k-nums[k] can be reached
        
        dp = [0]*(len(nums))
        dp[0] = True
        for i,k in enumerate(nums):
            
            for ik in range(1+k):
                if i+ik >= len(nums):
                    break
                dp[i+ik] = dp[i]
                if dp[-1]:
                    return dp[-1]
        print(dp)
        return dp[-1]
    
    
    def canJump1(self, nums: List[int]) -> bool:
        ## index k can be reached if k-nums[k] can be reached
        
        dp = [0]*(len(nums))
        dp[0] = True
        for i,k in enumerate(nums):
            
            for ik in range(k,0,-1):
                ## doing reverse order here. i.e. the furthest reachable backwards to the "furthest reached before"
                if i+ik >= len(nums):
                    continue
                if dp[i+ik]:
                    break
                    
                dp[i+ik] = dp[i]
                if dp[-1]:
                    return dp[-1]

        return dp[-1]
    

    def canJump(self, nums: List[int]) -> bool:
        ## the only problem is that 0 is in nums
        ## otherwise you can always leave!
        
        if 0 not in nums[:-1] or len(nums)<=1:
            return True
        
        i = 0 ## index
        r_end = 0 ##
        
        ## always go to the most possible end
        ## if not zero, keeps on going.
        while i<len(nums)-1:
            pass0 = False
            if nums[i]==0:
                
                for j in range(i):
                    if i-j<nums[j]:
                        pass0 = True
                        r_end = max(r_end, j+nums[j])
                        break
            else:
                pass0 = True
                r_end = max(r_end, i+nums[i])
            
            if not pass0:
                return False
            
            i = r_end
            #i += 1
        return True
        