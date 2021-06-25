'''719. Find K-th Smallest Pair Distance

Example 1:

Input: nums = [1,3,1], k = 1
Output: 0
Explanation: Here are all the pairs:
(1,3) -> 2
(1,1) -> 0
(3,1) -> 2
Then the 1st smallest distance pair is (1,1), and its distance is 0.
Example 2:

Input: nums = [1,1,1], k = 2
Output: 0
Example 3:

Input: nums = [1,6,1], k = 3
Output: 5
 

Constraints:

n == nums.length
2 <= n <= 104
0 <= nums[i] <= 106
1 <= k <= n * (n - 1) / 2


'''


import heapq
List = list()
class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()
        d = nums[-1] - nums[0]
        
        l, r = 0, d
        
        sz = len(nums)
        
        while l<r:
            mid = l + (r-l)//2
            j = 1
            cnt = 0
            for i in range(sz):
                while(j<sz and nums[j] - nums[i]<=mid):
                    j += 1
                cnt += (j - i - 1)
            if cnt < k:
                l = mid + 1
            
            
            else:
                r = mid
                    
        return l
        

    def smallestDistancePair_heap(self, nums: List[int], k: int) -> int:
        
        res = []
        
        for i,n in enumerate(nums):
            for s in nums[i+1:]:
                d = abs(n-s)
                heapq.heappush(res, -d)
                while(len(res) > k):
                    heapq.heappop(res)
        
        
        
        ans = heapq.heappop(res)

        return -ans
                    
                    
        