'''
264. Ugly Number II
Medium

3436

193

Add to List

Share
An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5.

Given an integer n, return the nth ugly number.

 

Example 1:

Input: n = 10
Output: 12
Explanation: [1, 2, 3, 4, 5, 6, 8, 9, 10, 12] is the sequence of the first 10 ugly numbers.
Example 2:

Input: n = 1
Output: 1
Explanation: 1 has no prime factors, therefore all of its prime factors are limited to 2, 3, and 5.
 

Constraints:

1 <= n <= 1690

hints:
1. The naive approach is to call 
    isUgly for every number until 
    you reach the nth one. 
2. An ugly number must be multiplied
    by either 2, 3, or 5 from 
    a smaller ugly number.
3. how to maintain the order of the ugly numbers?
'''
class Solution:
    def nthUglyNumber_stupid_heap(self, n: int) -> int:
        
        ## estimate how far we go
        if n<=3:
            return n
        
        N = n
        heap = []
        heapq.heapify(heap)
        def searching(num,cur_max, heap):
            ## note: we use negtive num
            if num in heap or num<cur_max:
                return
            tmp = cur_max
            while heap and len(heap)>N: ## note the Nth largest number is of index N-1
                tmp = max(cur_max,heapq.heappop(heap))
            cur_max = max(tmp, cur_max)
            heapq.heappush(heap, num)
            searching(num*2,cur_max, heap)
            searching(num*3,cur_max, heap)
            searching(num*5,cur_max, heap)
        cur_max = -float("inf")
        searching(-1,cur_max,(0,0,0),heap)
        while heap and len(heap)>N: ## note the Nth largest number is of index N-1
            heapq.heappop(heap)
        
        heap.sort()
        res = abs(heapq.heappop(heap))
        return res
    
    def nthUglyNumber_brutal(self, n: int) -> int:
        if n<=3:
            return n
        ## use the fact that the largest should not exceed the larget integer
        ## a bit tricky
        N = 2**31-1
        nums = []
        a = 1
        while a<N:
            b = a
            while b<N:
                c = b
                while c<N:
                    nums.append(c)
                    c*=5
                b *= 3
            a *= 2
        nums.sort()
        return nums[n-1]
    
    
    def nthUglyNumber_special_case(self, n: int) -> int:
        
        ## index of ugly number, that last processed by 2,3, or 5
        i2, i3, i5 = 0, 0, 0
        
        nums = [0]*n
        nums[0] = 1
        for k in range(1,n):
            res = min(nums[i2]*2, nums[i3]*3, nums[i5]*5)
            if nums[i2]*2 == res:
                i2 += 1
            if nums[i3]*3 == res:
                i3 += 1
            if nums[i5]*5 == res:
                i5 += 1
            nums[k] = res

        return nums[-1]
    
    def nthUglyNumber(self, n: int) -> int:
        
        ## index of ugly number, that last processed by 2,3, or 5
        dict_p = {k:0 for k in [2,3,5]}
        nums = [0]*n
        nums[0] = 1
        for k in range(1,n):
            res = float('inf')
            for v_p,idx_p in dict_p.items():
                res = min(res,nums[idx_p]*v_p)
            
            for v_p,idx_p in dict_p.items():
                if nums[idx_p]*v_p == res:
                    dict_p[v_p] += 1
 
            nums[k] = res

        return nums[-1]