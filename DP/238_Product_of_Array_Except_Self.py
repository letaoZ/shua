'''
238. Product of Array Except Self
Medium

10547

666

Add to List

Share
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

 

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
 

Constraints:

2 <= nums.length <= 105
-30 <= nums[i] <= 30
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
 

Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)
'''

class Solution:
    
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ## count zeros. if num of zeros >=2 return 0
        
        cnt_zeros = sum([n==0 for n in nums])
        res = [0]*(len(nums))
        if cnt_zeros >= 2:
            return res
        if cnt_zeros == 1:
            p = 1
            idx0 = -1
            for i in range(len(nums)):
                if nums[i]:
                    p *= nums[i]
                else:
                    idx0 = i
            res[idx0] = p
            return res
        ## left to right then right to left
        
        res[0] = 1
        for i in range(1,len(nums)): ## left to right
            res[i] = res[i-1]*nums[i-1]
        pright = 1
        for i in range(len(nums)-2,-1,-1): ## right to left
            res[i] *= (pright*nums[i+1])
            pright *= nums[i+1]
        return res
    def productExceptSelf0(self, nums: List[int]) -> List[int]:
        ## p_left[i] = product of numbers on the left of nums[i] without i
        ## p_right[i] = product of numbers on the right of nums[i] without i
        p_left = [0]*len(nums)
        p_right = [0]*len(nums)
        p_left[0] = 1
        p_right[-1] = 1
        idx_left_0 = len(nums)
        idx_right_0 = len(nums)
        for i in range(1,len(nums)):
            p_left[i] = p_left[i-1]*nums[i-1]
            if nums[i-1] == 0:
                idx_left_0 = i-1 ## starting from i, all zero
                break
                
        
        for i in range(len(nums)-2,-1,-1):
            p_right[i] = p_right[i+1]*nums[i+1]
            if nums[i+1] == 0:
                idx_right_0 = i+1
                break
        res = []        
        if idx_left_0 == idx_left_0 == len(nums):
            res = [p_right[i]*p_left[i] for i in range(len(nums))]
        elif idx_left_0 == idx_left_0 or idx_left_0 == len(nums) or idx_left_0 == len(nums):
            idx = min(idx_left_0, idx_right_0)
            res = [0]*len(nums)
            res[idx] = p_right[idx]*p_left[idx]
            
        else:
            res = [0]*len(nums)
            
        return res