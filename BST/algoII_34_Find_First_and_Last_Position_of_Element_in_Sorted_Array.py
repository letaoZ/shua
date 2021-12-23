'''
34. Find First and Last Position of Element in Sorted Array
Medium

8422

259

Add to List

Share
Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
Example 3:

Input: nums = [], target = 0
Output: [-1,-1]
 

Constraints:

0 <= nums.length <= 105
-109 <= nums[i] <= 109
nums is a non-decreasing array.
-109 <= target <= 109

'''

class Solution:
    def searchRange_N(self, nums: List[int], target: int) -> List[int]:
        l, r = 0, len(nums) - 1
        
        if r == -1:
            return [-1, -1]
        mid=0
        while l <= r:
            mid = l + (r-l)//2

            if nums[mid] < target:
                l = mid+1
            elif nums[mid] > target:
                r = mid - 1
            elif nums[mid] == target:
                break
        
        if nums[mid]!=target:
            return [-1, -1]
        l = r = mid
        while l>=0 and nums[l] == target:
            l -= 1
            
        while r<len(nums) and nums[r] == target:
            r += 1
            
        return [l+1, r-1]
    
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l, r = 0, len(nums) - 1
        
        if r == -1:
            return [-1, -1]
       
    
        def searching(nums, l, r, target, lower_bound = True):
            
            while l<=r:
                mid = l + (r-l)//2
                
                if nums[mid] == target:
                    if lower_bound:
                        if  mid == l or nums[mid-1]<target:
                            return mid
                        r -= 1 
                    elif not lower_bound:
                        if mid == r or nums[mid+1]>target:
                            return mid
                        l += 1
                elif nums[mid] < target:
                    l = mid + 1
                elif nums[mid] > target:
                    r = mid - 1
                    
            return -1
        
        lower_bound = searching(nums, 0, len(nums)-1, target,True)
        if lower_bound!=-1:
            upper_bound = searching(nums, 0, len(nums)-1, target,False)
        else:
            upper_bound = -1
            
        return [lower_bound, upper_bound]