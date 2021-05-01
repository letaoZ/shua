
'''
325. Maximum Size Subarray Sum Equals k
Medium


Given an integer array nums and an integer k, return the maximum length of a subarray that sums to k. If there isn't one, return 0 instead.

 

Example 1:

Input: nums = [1,-1,5,-2,3], k = 3
Output: 4
Explanation: The subarray [1, -1, 5, -2] sums to 3 and is the longest.
Example 2:

Input: nums = [-2,-1,2,1], k = 1
Output: 2
Explanation: The subarray [-1, 2] sums to 1 and is the longest.
 

Constraints:

1 <= nums.length <= 104
-104 <= nums[i] <= 104
-105 <= k <= 105
 

Follow Up: Can you do it in O(n) time?
'''

class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        
        ## psum[s]: keep track of partial sum equals, 
        ## smallest index
        ## if psum[s] = i, it means: sum(nums[:i]) = s
        psum = {}
        psum[0] = 0
        res = 0
        length = 0
        
        for i,n in enumerate(nums):
            res += n
            
            residual = res - k
            if residual in psum:
                length = max(length, i+1-psum[residual] )
            if res not in psum:
                psum[res] = i+1
                
        return length