'''
128. Longest Consecutive Sequence
Medium

12249

515

Add to List

Share
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

 

Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
 

Constraints:

0 <= nums.length <= 105
-109 <= nums[i] <= 109

'''
from typing import *
import collections
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        numSet = set(nums)
        resLen = 0
        for n in nums:
            
            ## first check if n is the beginning
            if n - 1 in numSet:
                continue
            
            ## then check if n + resLen is in nums
            ## i.e. check if we can reach longer?
            if n + resLen not in numSet:
                continue
            
            testLen = resLen
            while n + testLen in numSet:
                testLen -= 1
            if testLen != -1:
                continue
            
            testLen = resLen ## n together with n+1, .. n+resLen ALL in the numSet, so we get an extra resLen
            while n + testLen in numSet:
                testLen += 1
            resLen = testLen
            
        return resLen
        

    def longestConsecutive_sort(self, nums: List[int]) -> int:
        nums = list(set(nums))
        nums.sort()
        res = 0        
        i = 0
        while i < len(nums) - res:
            cnt = 1
            while i < len(nums) - ( 1) and nums[i] + 1 == nums[i + 1]:
                i += 1
                cnt += 1
            res = max(res, cnt)
            i += 1
            
        return res