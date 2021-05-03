
'''
628. Maximum Product of Three Numbers
Easy

Given an integer array nums, find three numbers whose product is maximum and return the maximum product.

 

Example 1:

Input: nums = [1,2,3]
Output: 6
Example 2:

Input: nums = [1,2,3,4]
Output: 24
Example 3:

Input: nums = [-1,-2,-3]
Output: -6
 

Constraints:

3 <= nums.length <= 104
-1000 <= nums[i] <= 1000
'''


import heapq
class Solution:
    def maximumProduct_sort(self, nums: List[int]) -> int:
        
        nums.sort()

        pos1, pos2, pos3 = nums[-3:]
        
        neg1,neg2 = nums[:2]
        
        res = max(pos1*pos2*pos3, neg1*neg2*pos3)
        
        return res
    
    def maximumProduct_heap(self, nums: List[int]) -> int:

    
        heapq.heapify(nums)
        neg1, neg2 = heapq.nsmallest(2,nums)
        pos1,pos2,pos3 = (heapq.nlargest(3,nums))
        
        res = max(pos1*pos2*pos3, neg1*neg2*pos1)
        return res