'''162. Find Peak Element

A peak element is an element that is strictly greater than its neighbors.

Given an integer array nums, find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the peaks.

You may imagine that nums[-1] = nums[n] = -∞.

You must write an algorithm that runs in O(log n) time.

 

Example 1:

Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and your function should return the index number 2.
Example 2:

Input: nums = [1,2,1,3,5,6,4]
Output: 5
Explanation: Your function can return either index number 1 where the peak element is 2, or index number 5 where the peak element is 6.
 

Constraints:

1 <= nums.length <= 1000
-231 <= nums[i] <= 231 - 1
nums[i] != nums[i + 1] for all valid i.
'''
List = list()
class Solution:
    
    def findPeakElement(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        while l<r:
            mid = l + (r - l) // 2
            if nums[mid] > nums[mid+1]:
                r = mid
            else:
                l = mid + 1
        return l
            
    def findPeakElement_O_N(self, nums: List[int]) -> int:
        
        i = 0
        sz = len(nums)
        m = 0
        
        if sz == 1:
            return 0
        if sz ==2:
            return 0 if nums[0]>nums[1] else 1
            
            
        while i<sz:
            l = i
            while i<sz-1 and nums[i]<nums[i+1]:
                i += 1
            if l==i:
                i += 1
                continue
            return i
        
        return 0