'''658. Find K Closest Elements
Medium

2237

334

Add to List

Share
Given a sorted integer array arr, two integers k and x, return the k closest integers to x in the array. The result should also be sorted in ascending order.

An integer a is closer to x than an integer b if:

|a - x| < |b - x|, or
|a - x| == |b - x| and a < b
 

Example 1:

Input: arr = [1,2,3,4,5], k = 4, x = 3
Output: [1,2,3,4]
Example 2:

Input: arr = [1,2,3,4,5], k = 4, x = -1
Output: [1,2,3,4]
 

Constraints:

1 <= k <= arr.length
1 <= arr.length <= 104
arr is sorted in ascending order.
-104 <= arr[i], x <= 104'''



import heapq
List = list()
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        '''
        Intuition :- The core idea behind this question is to find the start of the answer range efficiently. Therefore we try to find the start between the range [0, len(arr) - k - 1] (inclusive). We use binary search to do this and let's say everytime we try to evaluate mid as a possible answer start index. So the conditions to discard the search space in this situation would be :-

if given_val < arr[mid], move search space to low, mid - 1
if given_val >= arr[mid+k], move search space to mid + 1, high
if given_val is towards arr[mid], then move search space to low, mid - 1 else move search space to mid + 1, high
'''
        lo = 0
        hi = len(arr) - k - 1
        while(lo <= hi):
            mid = lo + (hi - lo) // 2
            st = arr[mid]
            end = arr[mid + k]
            if x < st:
                hi = mid - 1
            elif x >= end:
                lo = mid + 1
            else:
                if abs(x - st) <= abs(x - end):
                    hi = mid - 1
                else:
                    lo = mid + 1
        return arr[lo: lo + k]
    
    def findClosestElements_heap(self, arr: List[int], k: int, x: int) -> List[int]:
        ## didn't use input array being sorted    
        arr = [[-abs(tt-x), -tt] for tt in (arr)]
        heapq.heapify(arr)
        while len(arr)>k:
            heapq.heappop(arr)
            
        res = [-tt[1] for tt in arr]
        
        res.sort()
        return res
        

        
            