'''
713. Subarray Product Less Than K
Medium

Your are given an array of positive integers nums.

Count and print the number of (contiguous) subarrays where the product of all the elements in the subarray is less than k.

Example 1:
Input: nums = [10, 5, 2, 6], k = 100
Output: 8
Explanation: The 8 subarrays that have product less than 100 are: [10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6].
Note that [10, 5, 2] is not included as the product of 100 is not strictly less than k.
Note:

0 < nums.length <= 50000.
0 < nums[i] < 1000.
0 <= k < 10^6.
'''


        ## Note:
        ## the problem assume contiguous subarray prod > 0 and <k
class Solution:

    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        ## most recent submission:
        ## 2021-06-07
        if k == 0:
            return 0
        sz = len(nums)
        prod = 1
        prev_prod = collections.deque([1])
        res = 0
        left_end = 0
        nums = [1] + nums
        i = 1
        l = 0
        while i<len(nums):
            num = nums[i]
            if num == 0:
                # res += len(nums[i:])
                nums =  [1] + nums[i+1:]
                prod = 1
                l = 0
                i = 1
                continue
                
            if num>k:
                nums =  [1] + nums[i+1:]
                prod = 1
                l = 0
                i = 1
                continue
            prod *= num

            while l<i and prod>=k:
                l += 1
                prod /= nums[l]
            res += i - l

            

            i += 1
        return res

    def numSubarrayProductLessThanK_mem_consuming(self, nums: List[int], k: int) -> int:
        
        if k == 0:
            return 0
        sz = len(nums)
        prods = [1]*(sz+1)
        res = 0
        l = 0
        for i in range(1,sz+1):
            prods[i] = (prods[i-1]*nums[i-1] )
            ## no need to store prods
            while prods[i]/prods[l]>=k and l<i:
                l += 1
            res += (i-l)

        return res
    
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        ## two points
        if k == 0:
            return 0
         
        sz = len(nums)
        prods = 1
        res = 0
        l = 0
        for i in range(sz):
            prods *= nums[i]
            ## no need to store prods
            while prods>=k and l<=i:
                prods /= nums[l]
                l += 1
            res += (i-l + 1)

        return res
