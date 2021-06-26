'''786. K-th Smallest Prime Fraction

You are given a sorted integer array arr containing 1 and prime numbers, where all the integers of arr are unique. You are also given an integer k.

For every i and j where 0 <= i < j < arr.length, we consider the fraction arr[i] / arr[j].

Return the kth smallest fraction considered. Return your answer as an array of integers of size 2, where answer[0] == arr[i] and answer[1] == arr[j].

 

Example 1:

Input: arr = [1,2,3,5], k = 3
Output: [2,5]
Explanation: The fractions to be considered in sorted order are:
1/5, 1/3, 2/5, 1/2, 3/5, and 2/3.
The third fraction is 2/5.
Example 2:

Input: arr = [1,7], k = 1
Output: [1,7]
 

Constraints:

2 <= arr.length <= 1000
1 <= arr[i] <= 3 * 104
arr[0] == 1
arr[i] is a prime number for i > 0.
All the numbers of arr are unique and sorted in strictly increasing order.
1 <= k <= arr.length * (arr.length - 1) / 2


'''
import heapq

List = list()
class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        l, r = 0., 1.
        p, q = 0,1
        
        n = len(arr) 
        ## time = n*log(max(arr)^2)
        
        while l<r:
            m = (l+r) / 2
            j = n-1
            cnt = 0
            p = 0
            ## cnt the number of fraction <= m
            for i in range(n):
                while(j>=0 and arr[i]/arr[n-1-j] > m):
                    j-= 1
                    
                cnt += (j+1)
                if j>=0 and arr[i]/arr[n-1-j]> p/q:
                    p, q = arr[i], arr[n-1-j]
            
            if (cnt == k):
                return [p,q]
            elif cnt<k:
                l = m
            else:
                r = m
                
        
    def kthSmallestPrimeFraction_heap_ordered_matrix(self, arr: List[int], k: int) -> List[int]:
        ## consider matrix[i][j] = arr[i]/arr[j]
        ## then the row and columns of the matrix are both in ascending order

        sz = len(arr)
        q = []
        for i in range(0,sz-1):
            ## first column must have min
            ## (i,0) -- 0 corresponds column 0, but sz-1th number of the array
            heapq.heappush(q,(arr[i]/arr[sz-1],i, 0))
        
        while k-1>0:
            v, row, col =heapq.heappop(q)
            x, y = row, sz-1-col
            if y-1>x:
                y -= 1
                heapq.heappush(q, (arr[x]/arr[y], x, sz-1-y))

            k -= 1

        v, row, col =heapq.heappop(q)
        x, y = row, sz-1-col
        return [arr[x], arr[y]]
        
    def kthSmallestPrimeFraction_heap(self, arr: List[int], k: int) -> List[int]:
        q = []
        sz = len(arr)
        for i in range(sz):
            for j in range(i+1,sz):
                frac = arr[i]/arr[j]
                heapq.heappush(q,(-frac, i,j))
                while len(q)>k:
                    heapq.heappop(q)
        _,a,b = heapq.heappop(q)
        return [arr[a], arr[b]]
    def kthSmallestPrimeFraction_sort(self, arr: List[int], k: int) -> List[int]:
        
        nums = [(arr[j]/arr[i],j,i) for i in range(1,len(arr)) for j in range(i) ]
        
        nums.sort()
        _,a,b = nums[k-1]
        return [arr[a],arr[b]]