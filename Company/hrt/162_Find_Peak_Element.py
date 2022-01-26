'''
162. Find Peak Element
Medium

5115

3428

Add to List

Share
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


class Solution:
    
    def findPeakElement_left_bound(self, nums: List[int]) -> int:

    # def findPeakElement(self, nums: List[int]) -> int:
        l, r = 0, len(nums)
        while l<r:
            mid = l + (r - l) // 2
            if (mid+1 == len(nums) ) or (mid+1<len(nums) and nums[mid] > nums[mid+1]):
                r = mid
            
            else:
                l = mid + 1
        return l
    def findPeakElement_with_equal_consideration(self, nums: List[int]) -> int:
        ## divide
        
        l, r = 0, len(nums) ## may return left; we have stop condition within the while. good
        if len(nums) ==1 :
            return  0
        N  = len(nums)
        
        ## consider equality
        def searching(l,r):
            while l<=r:
                mid = l + (r-l) // 2
                ## conditions for termination
                if 0 < mid < N-1 and nums[mid-1] < nums[mid] > nums[mid+1]:
                    return mid
                elif 0 == mid and nums[mid] > nums[mid+1]:
                    return mid
                elif mid == N-1 and nums[mid-1] < nums[mid]:
                    return mid
                elif mid < N-1 and nums[mid] < nums[mid+1]:
                    l = mid + 1
                elif mid>0 and nums[mid-1] > nums[mid]:
                    r = mid - 1
                elif mid == 0 or mid == N - 1:
                    return mid
                print("equal")
                print(mid)
                print(nums[mid-1:mid+2])
                ## case where we have nums[mid-1] == nums[mid] or nums[mid] == nums[mid+1]
                if mid>0 and nums[mid-1] == nums[mid]:
                    
                    res1 = searching(l, mid-2)
                    if res1 != -1:
                        return res1
                    res2 = searching(mid+1, r)
                    if res2 != -1:
                        return res2
                if mid<N-1 and nums[mid+1] == nums[mid]:
                    res1 = searching(mid+2,r)
                    if res1 != -1:
                        return res1
                    res2 = searching(l,mid-1 )
                    if res2 != -1:
                        return res2
                print("end equal")
            return -1
        
        res = searching(l,r)
        if not (res == 0 or res == N-1 or res == -1):
            return res
        else:
            if nums[0] > nums[1]:
                return 0
            if nums[-1]> nums[-2]:
                return N-1
    
            
    def findPeakElement_brutal(self, nums: List[int]) -> int:
        
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
        
    def findPeakElement_left_right_bound(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        if r == 0:
            return 0
        
        while l<=r:
            mid = l + (r-l) // 2
            if mid < len(nums)-1 and mid>0 and nums[mid-1]<nums[mid] and nums[mid]>nums[mid+1]:
                return mid
            elif mid == len(nums) - 1 and nums[mid-1]<nums[mid]:
                return mid
            elif mid == 0 and nums[mid]> nums[mid+1]:
                return mid
            elif mid < len(nums) - 1 and nums[mid]<nums[mid+1]:
                l = mid + 1
            elif mid > 0 and nums[mid]<nums[mid-1]:
                r = mid-1
            elif mid == len(nums) - 1 or mid == 0:
                break
                
        if l>0 and l<len(nums)-1 and nums[l]>nums[l-1] and nums[l] > nums[l+1]:
            return l
        else:
            return -1