'''
1060. Missing Element in Sorted Array
Medium

1140

45

Add to List

Share
Given an integer array nums which is sorted in ascending order and all of its elements are unique and given also an integer k, return the kth missing number starting from the leftmost number of the array.

 

Example 1:

Input: nums = [4,7,9,10], k = 1
Output: 5
Explanation: The first missing number is 5.
Example 2:

Input: nums = [4,7,9,10], k = 3
Output: 8
Explanation: The missing numbers are [5,6,8,...], hence the third missing number is 8.
Example 3:

Input: nums = [1,2,4], k = 3
Output: 6
Explanation: The missing numbers are [3,5,6,7,...], hence the third missing number is 6.
 

Constraints:

1 <= nums.length <= 5 * 104
1 <= nums[i] <= 107
nums is sorted in ascending order, and all the elements are unique.
1 <= k <= 108
 

Follow up: Can you find a logarithmic time complexity (i.e., O(log(n))) solution?
'''

class Solution:
    def missingElement_brutal(self, nums: List[int], k: int) -> int:
        
        n0 = nums[0]
        i = 0
        res = n0
        while k>0 and i<len(nums):
            if n0 not in nums:
                k -= 1
                res = n0
                
            elif n0 in nums:
                i += 1
            
            n0 += 1
        return n0 + k - 1
    
    
    def missingElement(self, nums: List[int], k: int) -> int:
        n0 = nums[0]
        
        l = 0
        r = len(nums) - 1
        ## num of numbers  missing between nums[idx0] and nums[idx1]: 
        #           nums[idx1] - ((idx1 - idx0) + nums[idx0])
        total_missing = nums[r] - (r-0 + nums[0])
        if total_missing < k:
            return nums[r] + (k - total_missing)
        
        while l<=r and k>0:
            mid = l + (r - l)//2
            # print(f"left {l}, value {nums[l]}")
            # print(f"mid {mid}, value {nums[mid]}")
            # print(f"right {r}, value {nums[r]}")
            # print()
            if mid == l:
                break
            n_left_missing = nums[mid] - (mid-l +nums[l])
            n_right_missing = nums[r] - (r - mid +nums[mid])
            if n_left_missing<k:
                k -= n_left_missing
                l = mid
            elif n_left_missing>=k:
                r = mid
        return nums[l] + k