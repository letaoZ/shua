'''
260. Single Number III
Medium

3701

177

Add to List

Share
Given an integer array nums, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once. You can return the answer in any order.

You must write an algorithm that runs in linear runtime complexity and uses only constant extra space.

 

Example 1:

Input: nums = [1,2,1,3,2,5]
Output: [3,5]
Explanation:  [5, 3] is also a valid answer.
Example 2:

Input: nums = [-1,0]
Output: [-1,0]
Example 3:

Input: nums = [0,1]
Output: [1,0]
 

Constraints:

2 <= nums.length <= 3 * 104
-231 <= nums[i] <= 231 - 1
Each integer in nums will appear twice, only two integers will appear once.
'''
from typing import *

class Solution:

    def singleNumber(self, nums: List[int]) -> List[int]:
        
        
        k = nums[0]
        for m in nums[1:]:
            k = (k^m)
        ## k = d1 xor d2
        
        ## Since d1 and d2 are differe,t there must be an ith bit of k is 1, then d1 and d2 different
        ## we divide up the nums using k
        ## one group = ith bit is 1; the other group = ith bit is 0
        ## so d1 and d2 will be in different group, duplicate nums will be in the same group
        
        d1, d2 = 0, 0
        lowbit = k & (-k) ## the lowest bit that is not 0
        for n in nums:
            if (n & lowbit)==0:
                d1 = (d1^n)
            else:
                d2 = (d2^n)
        return [d1, d2]