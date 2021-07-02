'''644. Maximum Average Subarray II
Hard


Find a contiguous subarray whose length is greater than or equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted.

 

Example 1:

Input: nums = [1,12,-5,-6,50,3], k = 4
Output: 12.75000
Explanation:
- When the length is 4, averages are [0.5, 12.75, 10.5] and the maximum average is 12.75
- When the length is 5, averages are [10.4, 10.8] and the maximum average is 10.8
- When the length is 6, averages are [9.16667] and the maximum average is 9.16667
The maximum average is when we choose a subarray of length 4 (i.e., the sub array [12, -5, -6, 50]) which has the max average 12.75, so we return 12.75
Note that we do not consider the subarrays of length < 4.
Example 2:

Input: nums = [5], k = 1
Output: 5.00000
 

Constraints:

n == nums.length
1 <= k <= n <= 104
-104 <= nums[i] <= 104
'''

import heapq
List = list()
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        l, r = min(nums), max(nums)
        
        def condition(mid, k,nums):
            tmp = [num - mid for num in nums ]
            psum = sum(tmp[:k])
            if psum >= 0: return True
            frontsum = 0
            for i in range(k,len(tmp)):
                psum += tmp[i]
                frontsum += tmp[i-k]
                
                if frontsum <0 :
                    psum -= frontsum
                    frontsum = 0
                if psum>=0:
                    return True
                
            return False
        ## use tolerance here
        ## And we have l = mid!! because you cannot add 1!
        
        while r-l>1e-5:
            mid = l + (r-l)/2
            
            if condition(mid, k, nums):
                l = mid
            else:
                r = mid
        
        return l
            
    
    def findMaxAverage_too_slow(self, nums: List[int], k: int) -> float:
        
        psum = [sum(nums[i:i+k]) for i in range(len(nums)-k+1)]
        sz = len(nums)
        q = [-s/k for s in psum]
        res = -float('inf')
        heapq.heapify(q)
        
        ## Note, we can find the condition on a_n
        ## when average(a_i, i=1,..n-1) < average(a_i, i=1,... n)
        while k<len(nums):
            psum_tmp = []
            res =max(res, -heapq.heappop(q))
            q = []
            for j,s in enumerate(psum):
                if j+k<sz:
                    new_s = s+nums[j+k]
                    psum_tmp.append(new_s)
                    if nums[j+k]>s/k:
                        heapq.heappush(q, -new_s/(k+1))
                        
            if len(q) == 0:
                break
            psum = psum_tmp
            k += 1
            
        # res = -heapq.heappop(q)
        if q:
            res = max(res, -heapq.heappop(q))
        return res