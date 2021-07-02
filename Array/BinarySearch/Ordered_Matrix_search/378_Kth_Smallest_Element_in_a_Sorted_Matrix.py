

import heapq
List = list()

class Solution:
    def kthSmallest_binarySearch(self, matrix: List[List[int]], k: int) -> int:
        ## error checking algo
        ## time = log(Max(matrix) - Min(matrix))*m
        m, n = len(matrix), len(matrix[0])
        if k>= m*n:
            return matrix[-1][-1]
        
        l, r = matrix[0][0], matrix[-1][-1]
        def condition(mid, k):
            
            
            cnt = 0
            j = n-1
            for i in range(m):
                while(j>=0 and matrix[i][j] > mid):
                    j -= 1
                cnt += (j+1)
            return (cnt < k)
        while l<r:
            mid = l + (r-l) // 2
            
            if condition(mid, k):
                l = mid + 1
                
            else:
                r = mid
                
        return l
            
            
    def kthSmallest_heap(self, matrix: List[List[int]], k: int) -> int:
        ## heap algo
        ## m = len(matrix). 
        # (m+k)log(m)
        m, n = len(matrix), len(matrix[0])
        if k>= m*n:
            return matrix[-1][-1]
        
        q = []
        # stirling's approximation. ln(n!) = nln(n) - n + O(lnn) = O(nln n) 
        # time here: mlogm
        for i in range(m):
            heapq.heappush(q, (matrix[i][0], i, 0))
            
        # time here: klogm
        while k>0:
            v, x, y = heapq.heappop(q)
            if y+1<n:
                heapq.heappush(q, (matrix[x][y+1], x, y+1))
            k -= 1
            
        return v