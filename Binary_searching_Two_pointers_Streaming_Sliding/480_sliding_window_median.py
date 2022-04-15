'''
480. Sliding Window Median
Hard

2108

130

Add to List

Share
The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. So the median is the mean of the two middle values.

For examples, if arr = [2,3,4], the median is 3.
For examples, if arr = [1,2,3,4], the median is (2 + 3) / 2 = 2.5.
You are given an integer array nums and an integer k. There is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

Return the median array for each window in the original array. Answers within 10-5 of the actual value will be accepted.

 

Example 1:

Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [1.00000,-1.00000,-1.00000,3.00000,5.00000,6.00000]
Explanation: 
Window position                Median
---------------                -----
[1  3  -1] -3  5  3  6  7        1
 1 [3  -1  -3] 5  3  6  7       -1
 1  3 [-1  -3  5] 3  6  7       -1
 1  3  -1 [-3  5  3] 6  7        3
 1  3  -1  -3 [5  3  6] 7        5
 1  3  -1  -3  5 [3  6  7]       6
Example 2:

Input: nums = [1,2,3,4,2,3,1,4,2], k = 3
Output: [2.00000,3.00000,3.00000,3.00000,2.00000,3.00000,2.00000]
 

Constraints:

1 <= k <= nums.length <= 105
-231 <= nums[i] <= 231 - 1'''

from sortedcontainers import SortedDict
class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        if k == 1: return nums
        
        
        ## double heap
        ## max in smaller side -- maxheap
        ## min in larger side -- minheap: 1>=len(larger) - len(smaller)>=0
        l = []
        s = []
        def balance_heaps(num, l, s):
            if (not l) or num>= l[0]:
                heapq.heappush(l, num)
            else:
                heapq.heappush(s, -num)
                
            while len(l)-len(s)>1:
                heapq.heappush(s,-heapq.heappop(l))
        
            while len(l)-len(s)<0:
                heapq.heappush(l,-heapq.heappop(s))
            
        for i in range(k):
            balance_heaps(nums[i],l,s)
        
        oddity = k%2
        res = []

        for i in range(k,len(nums)+1):
            ## first insert result
            if oddity:
                res.append(l[0])
            else:
                res.append((l[0] - s[0])/2.)
                
            rmNum = nums[i-k]
            if rmNum in l:
                if rmNum == l[0]:
                    heapq.heappop(l)
                else:
                    l.remove(rmNum)
                    heapq.heapify(l)
            elif -rmNum in s:
                if -rmNum == s[0]:
                    heapq.heappop(s)
                else:
                    s.remove(-rmNum)
                    heapq.heapify(s)
            if i == len(nums):
                break
            balance_heaps(nums[i],l,s)
        return res
        
    def medianSlidingWindow_brutal(self, nums: List[int], k: int) -> List[float]:
        
        res = []
        m0 = k//2
        m1 = (k-1)//2
        for i in range(k,len(nums)+1):
            tmp = [_ for _ in nums[i-k:i]]
            tmp.sort()
            res.append( (tmp[m0] + tmp[m1])/2 )
        return res