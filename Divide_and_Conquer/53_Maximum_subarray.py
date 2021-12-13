
'''
53. Maximum Subarray
Easy

16598

778

Add to List

Share
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

A subarray is a contiguous part of an array.

 

Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Example 2:

Input: nums = [1]
Output: 1
Example 3:

Input: nums = [5,4,-1,7,8]
Output: 23
 

Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
 

Follow up: If you have figured out the O(n) solution, 
try coding another solution using the divide and conquer approach, which is more subtle.
'''
class Solution:
    def maxSubArray_brutal(self, nums: List[int]) -> int:
        '''psum[i][j]: sum of nums[i:j]'''
        '''compute all psums, brutal, exceeding time limit'''
        N = len(nums)
        psum = [ [0]*(N+1) for _ in range(N)]
        
        for i in range(N):
            for j in range(i+1, N+1):
                psum[i][j] = psum[i][j-1] + nums[j-1]
                
                
        res = max([max([psum[i][j] for j in range(i+1, N+1)]) for i in range(N)])
        return res
    
    def maxSubArray_dp(self, nums: List[int]) -> int:
        
        ## psum[k] := first compute sum(nums[:k])
        N = len(nums)
        psum = [0] *(N+1)
        for k in range(1, N+1):
            psum[k] = psum[k-1] + nums[k-1]
            
        l,r=0, 0
        res = max(nums)
        min_left_value = float('inf')
        
        N = len(psum)
        while l< N:
            while l<N-1 and psum[l]>psum[l+1]:
                l += 1
            r = l+1
            
            while r<N-1 and psum[r]<=psum[r+1]:
                r += 1
            if r>=N:
                break
            min_left_value = min(min_left_value, psum[l])
            res = max(res, psum[r] - min_left_value)
            l = r+1
            
        return res
    
    
    def maxSubArray_divide_conquer(self, nums: List[int]) -> int:
        ## divide and conquer
        if len(nums) == 1:
            return nums[0]
    

        def divide_conquer(nums,l,r):
            if l>r:
                return nums[0]
        
            mid = l + (r-l)//2
            
            ## find the max of left sum without mid
            ## find the max of the rigth sum without mid
            lsum, rsum = divide_conquer(nums,l,mid-1), divide_conquer(nums,mid+1,r)
            
            
            
            ## now we want to find, including mid, the max continues sum you can get
            ml, mr = 0, 0
            psum = 0
            for i in range(mid-1,l-1,-1):
                psum += nums[i]
                ml = max(psum, ml);
                
            psum = 0
            for i in range(mid+1,r+1):
                psum += nums[i]
                mr = max(psum, mr);
            midsum = ml + mr + nums[mid]
            
            
            return max(lsum, rsum, midsum)
        
        return divide_conquer(nums,0,len(nums)-1)