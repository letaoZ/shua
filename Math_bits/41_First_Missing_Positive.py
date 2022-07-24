'''
41. First Missing Positive
Hard

10641

1397

Add to List

Share
Given an unsorted integer array nums, return the smallest missing positive integer.

You must implement an algorithm that runs in O(n) time and uses constant extra space.

 

Example 1:

Input: nums = [1,2,0]
Output: 3
Example 2:

Input: nums = [3,4,-1,1]
Output: 2
Example 3:

Input: nums = [7,8,9,11,12]
Output: 1
 

Constraints:

1 <= nums.length <= 5 * 105
-231 <= nums[i] <= 231 - 1
'''
from typing import *
class Solution:
    
    def firstMissingPositive(self, nums: List[int]) -> int:
        '''
        first missing positive must be between [1, len(nums) + 1]
        e.g. nums = [1,2,3], first missing is 3 + 1
            nums = [-1,1,5], first missing is 2 between [1,3+1]
        '''
        nums.append(0)
        L = len(nums)
        
        ## map index to visisted
        ## index of numbers 0-> other, 1->1, 2->2, .. L-1->L-1; 
        ## NOTE: we padded nums with an extra element. So if we visit ALL elements < L, then result must of L
        for i in range(L):
            if nums[i] < 0 or nums[i] >= L: ##
                nums[i] = 0
        for i in range(L):
            nums[nums[i]%L] += L
        for i in range(1,L):
            if nums[i] // L == 0:
                return i
            
        return L
                

    def firstMissingPositive_brutal(self, nums: List[int]) -> int:
        m = min(nums)
        if m > 1:
            return 1
        
        M = max(nums)
        if M <= 0:
            return 1
        
        # if M - m + 1 == len(nums):
        #     return M + 1
        
        visited = [0] * (M - m + 1)
        for n in nums:
            visited[n-m] = 1
        
        if m <= 0:
            for k in range( abs(m) + 1, len(visited)):
                if not visited[k]:
                    return k + m
        
        else: ## when m == 1
            for k in range(1, len(visited)):
                if not visited[k]:
                    return k + 1
                
                
        return M + 1