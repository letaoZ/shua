'''643. Maximum Average Subarray I

You are given an integer array nums consisting of n elements, and an integer k.

Find a contiguous subarray whose length is equal to k that has the maximum average value 
and return this value. Any answer with a calculation error less than 10-5 will be accepted.

 

Example 1:

Input: nums = [1,12,-5,-6,50,3], k = 4
Output: 12.75000
Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75
Example 2:

Input: nums = [5], k = 1
Output: 5.00000
 

Constraints:

n == nums.length
1 <= k <= n <= 105
-104 <= nums[i] <= 104
'''

List = list()

class Solution:
    def findMaxAverage_binary(self, nums: List[int], k: int) -> float:
        ## NOTE: binary is slower here!
        l, r = min(nums), max(nums)
        def condition(mid, k,nums):
            aux = [nums[i]-mid for i in range(len(nums))]
            
            psum = sum(aux[:k])
            
            if psum >= 0:
                return True

            for i in range(k,len(nums)):
                psum += aux[i]
                psum -= aux[i-k]
                if psum>=0:
                    return True
            return False
                
        while r-l>=1e-5:
            mid = l + (r-l)/2
            
            if condition(mid, k , nums):
                l = mid
            else:
                r = mid
        return l
        
    def findMaxAverage_n(self, nums: List[int], k: int) -> float:
        psum = sum(nums[:k])
        res = psum/k
        for i in range(k,len(nums)):
            psum -= nums[i-k]
            psum += nums[i]
            res = max(res, psum/k)
            
        return res