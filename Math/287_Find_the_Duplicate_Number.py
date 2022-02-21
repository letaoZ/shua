''
'''
287. Find the Duplicate Number
Medium

10749

1111

Add to List

Share
Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

There is only one repeated number in nums, return this repeated number.

You must solve the problem without modifying the array nums and uses only constant extra space.

 

Example 1:

Input: nums = [1,3,4,2,2]
Output: 2
Example 2:

Input: nums = [3,1,3,4,2]
Output: 3
 

Constraints:

1 <= n <= 105
nums.length == n + 1
1 <= nums[i] <= n
All the integers in nums appear only once except for precisely one integer which appears two or more times.
 

Follow up:

How can we prove that at least one duplicate number must exist in nums?
Can you solve the problem in linear runtime complexity?
'''

class Solution:
    def findDuplicate_N(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                return nums[i]
            
    def findDuplicate_bst(self, nums: List[int]) -> int:
        nums.sort()
        ## no worry about bound return
        if nums[0] == nums[1]:
            return nums[0]
        elif nums[-1] == nums[-2]:
            return nums[-1]
        
        
        N = len(nums) - 1
        l, r = 0, len(nums)

        ## if no extra, nums[i] == i + 1
        while l<r:
            mid = l + (r - l) // 2
            if mid + 1 == nums[mid]: ## left
                l = mid ## return left
            elif mid + 1 > nums[mid]:
                r = mid - 1
            elif mid + 1 < nums[mid]:
                l = mid
        return nums[l]
    
    
    def findDuplicate(self, nums: List[int]) -> int:

        ## idea:
        ## nums: 1,3,4,2,2
        ## start from index = nums[0] == 1
        ##  the index 1 goes to index nums[1]=3
        ##  the index 3 goes to index nums[3]=2
        ##  the index 2 goes to index nums[2]=4
        ##  the index 4 goes to index nums[4]=2
        ## so there is a cycle: 1->3>2->4->2, the duplicate is the intersection of the cycle with the path at 2
        
        slow = nums[0]
        fast = nums[slow]
        ## there is a cycle
        while slow!=fast:
            slow = nums[slow]
            fast = nums[nums[fast]]
            
        fast = 0
        while slow!=fast:
            fast = nums[fast]
            slow = nums[slow]
        return slow