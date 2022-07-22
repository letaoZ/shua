'''
75. Sort Colors
Medium

11069

436

Add to List

Share
Given an array nums with n objects colored red, white, or blue, 
sort them in-place so that objects of the same color are adjacent, 
with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.

Example 1:

Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
Example 2:

Input: nums = [2,0,1]
Output: [0,1,2]

Constraints:

n == nums.length
1 <= n <= 300
nums[i] is either 0, 1, or 2.

Follow up: Could you come up with a one-pass algorithm using only constant extra space?
'''
from typing import *

class Solution:
    
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        ## i0 := last index of 0; i1 := last index of 1; i2 := first index of 2
        i0, i1, i2 = 0, 0, len(nums) - 1
        ## iK := index where number K starts, K = 0, 1, 2
        while i1 <= i2:
            if nums[i1] == 2:
                nums[i1], nums[i2] = nums[i2], 2
                i2 -= 1
            elif nums[i1] == 0:
                nums[i0], nums[i1] = nums[i1], nums[i0]
                i0 += 1
                i1 += 1
            elif nums[i1] == 1:
                
                i1 += 1
        
        
    def sortColors_cnt(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        cnts = [0]*3
        for n in nums:
            cnts[n] += 1
        
        ci = 0
        for i in range(len(nums)):
            while cnts[ci] == 0:
                ci += 1

            nums[i] = ci
            cnts[ci] -= 1
            
        