'''
238. Product of Array Except Self
Medium

Given an integer array nums, return an array answer such that answer[i] is 
equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

 

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
 

Constraints:

2 <= nums.length <= 105
-30 <= nums[i] <= 30
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
 

Follow up:

Could you solve it in O(n) time complexity and without using division?
Could you solve it with O(1) constant space complexity? (The output array does not count as extra space for space complexity analysis.)


'''


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
            
        ans = [0]*(len(nums))    

        ## keep track where zero is
        ## if there are more than 1 zeros, then all prod=0
        
        loc0 = -1
        P = 1
        for i,n in enumerate(nums):
            if n==0:
                if loc0>=0:
                    return ans
                else: 
                    loc0 = i
                    
            else:
                P *= n
                
                
        if loc0 >=0:
            ans[loc0] = P
        else:
            ans = [int(P/n) for n in nums]
        return ans        


    ## follow up question:
    ## not use division
    def productExceptSelf_wo_division(self, nums: List[int]) -> List[int]:

        ##psum so far without including current number
        psum = [1]*len(nums)
        P = 1
        for i in range(len(nums)):
            psum[i] = P
            P *= nums[i]

        ## psum backwards
        P = 1

        for i in range(len(nums)-1,-1,-1):
            psum[i] *= P
            P *= nums[i]

        return psum
    
                