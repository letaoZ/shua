'''
523. Continuous Subarray Sum
Medium

Given an integer array nums and an integer k, return true if nums has a continuous subarray of size at least two whose elements sum up to a multiple of k, or false otherwise.

An integer x is a multiple of k if there exists an integer n such that x = n * k. 0 is always a multiple of k.

 

Example 1:

Input: nums = [23,2,4,6,7], k = 6
Output: true
Explanation: [2, 4] is a continuous subarray of size 2 whose elements sum up to 6.
Example 2:

Input: nums = [23,2,6,4,7], k = 6
Output: true
Explanation: [23, 2, 6, 4, 7] is an continuous subarray of size 5 whose elements sum up to 42.
42 is a multiple of 6 because 42 = 7 * 6 and 7 is an integer.
Example 3:

Input: nums = [23,2,6,4,7], k = 13
Output: false
 

Constraints:

1 <= nums.length <= 105
0 <= nums[i] <= 109
0 <= sum(nums[i]) <= 231 - 1
1 <= k <= 231 - 1
'''

import collections
class Solution:
    def checkSubarraySum_slow(self, nums, k) -> bool:
        sz=len(nums)
        if sz == 1:
            return False
        
        psum = [0]*(1+sz)

        for i in range(1,sz+1):
            psum[i] = psum[i-1] + nums[i-1]

        ## too slow: O(sz^2)
        for l in range(2,sz):
            for e in range(l, sz+1):
                if psum[e] - psum[e-l] == k:
                    print(e, l)
                    return True
        return False
    
    def checkSubarraySum(self, nums, k) -> bool:

        ## same as before, use dp
        sz = len(nums)

        ## store the smallest index with psum
        ## i.e. the first time that a sum show up
        psum = dict()
        psum[0] = 0
        res = 0

        for i,n in enumerate(nums):
            res += n
            res %= k
            if res in psum:
                if psum[res]<=i-1:
                    return True
            else:
                ## Note here we use index+1 as sum(nums[:i+1]) inclusive
                ## So psum[0] = 0 makes more sense!
                psum[res] = i+1

        return False



nums = [1,3,3,6]
k = 6

solu = Solution()
solu.checkSubarraySum(nums, k)