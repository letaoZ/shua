'''373. Find K Pairs with Smallest Sums
Medium

You are given two integer arrays nums1 and nums2 sorted in ascending order and an integer k.

Define a pair (u, v) which consists of one element from the first array and one element from the second array.

Return the k pairs (u1, v1), (u2, v2), ..., (uk, vk) with the smallest sums.

 

Example 1:

Input: nums1 = [1,7,11], nums2 = [2,4,6], k = 3
Output: [[1,2],[1,4],[1,6]]
Explanation: The first 3 pairs are returned from the sequence: [1,2],[1,4],[1,6],[7,2],[7,4],[11,2],[7,6],[11,4],[11,6]
Example 2:

Input: nums1 = [1,1,2], nums2 = [1,2,3], k = 2
Output: [[1,1],[1,1]]
Explanation: The first 2 pairs are returned from the sequence: [1,1],[1,1],[1,2],[2,1],[1,2],[2,2],[1,3],[1,3],[2,3]
Example 3:

Input: nums1 = [1,2], nums2 = [3], k = 3
Output: [[1,3],[2,3]]
Explanation: All possible pairs are returned from the sequence: [1,3],[2,3]
 

Constraints:

1 <= nums1.length, nums2.length <= 104
-109 <= nums1[i], nums2[i] <= 109
nums1 and nums2 both are sorted in ascending order.
1 <= k <= 1000


'''

import heapq
List = list()

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        
        ## NOTE: this problem DOES not require to return ALL kth pair
        ## eg: 
#         if input is [1,2,3],[1,2,3], k = 4. 
#         sums are 2, [1,1]; 3, [1,2],[2,3]; 4: [1,3],[2,2],[3,1]. 
#         So the first four pairs are More than just 4 pairs...
        
            
        m = len(nums1)
        n = len(nums2)
        if k>= m*n:
            return [[x,y] for x in nums1 for y in nums2]
        
        q = []
        for i in range(m):
            heapq.heappush(q, (nums1[i] + nums2[0], 0, i))
                
        res = []
        while k>0:
            ss, y, x = heapq.heappop(q)
            res.append([nums1[x],nums2[y]])
            if y+1<n:
                heapq.heappush(q, (nums1[x] + nums2[y+1], y+1, x))
                
                
            k -= 1
        
        
        return res
            
            
    def kSmallestPairs_find_the_sum(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        m = len(nums1)
        n = len(nums2)
        if k>= m*n:
            return [[x,y] for x in nums1 for y in nums2]
        
        
        l, r = nums1[0]+nums2[0], nums1[-1] + nums2[-1]
        
        def condition(mid, k):
            
            j = n-1
            ## cnt: total numbs that are <= mid
            cnt = 0
            for num in nums1:
                while j>=0 and num+nums2[j]>mid: j-=1
                cnt += (j+1)
                
            return (cnt < k)

        while l<r:
            mid = l + (r-l)//2
            
            if condition(mid, k):
                l = mid+1
            else:
                r = mid
                
                
        
        
         