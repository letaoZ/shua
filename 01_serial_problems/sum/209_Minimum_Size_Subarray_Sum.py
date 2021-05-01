'''
209. Minimum Size Subarray Sum
Medium

Given an array of positive integers nums and a positive integer target, return the minimal length of a contiguous subarray [numsl, numsl+1, ..., numsr-1, numsr] of which the sum is greater than or equal to target. If there is no such subarray, return 0 instead.

 

Example 1:

Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.
Example 2:

Input: target = 4, nums = [1,4,4]
Output: 1
Example 3:

Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0
 

Constraints:

1 <= target <= 109
1 <= nums.length <= 105
1 <= nums[i] <= 105
 

Follow up: If you have figured out the O(n) solution, 
try coding another solution of which the time complexity 
is O(n log(n)).
'''

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        ## important that 
        ## all numbers are positive
        
        if target == 0:
            return 0
        if sum(nums)<target:
            return 0
        
        tmp = [nn for nn in nums if nn>=target]
        if len(tmp) > 0: 
            return 1
        

        
        
        cur_l = 0
        
        psum = 0
        
        res = len(nums)
        
        for i,n in enumerate(nums):
            
            psum += n
            ## Note current left end is open, i.e. remove everything
            ## whose index < cur_l!!!
            while psum >= target and cur_l <=i:
                res  = min(res, i - cur_l +1)
                psum -= nums[cur_l] 
                cur_l += 1
                
            
            
                
            
                
        return res