'''668. Kth Smallest Number in Multiplication Table


Nearly everyone has used the Multiplication Table. The multiplication table of size m x n is an integer matrix mat where mat[i][j] == i * j (1-indexed).

Given three integers m, n, and k, return the kth smallest element in the m x n multiplication table.

 

Example 1:


Input: m = 3, n = 3, k = 5
Output: 3
Explanation: The 5th smallest number is 3.
Example 2:


Input: m = 2, n = 3, k = 6
Output: 6
Explanation: The 6th smallest number is 6.
 

Constraints:

1 <= m, n <= 3 * 104
1 <= k <= m * n


'''
class Solution:

    def findKthNumber(self, m: int, n: int, k: int) -> int:
        
        l, r = 0, m*n
        if m>n:
            m, n = n, m
        
        
        ## NOTE: condition is always return when we need left + 1
        ## so left will NEVER include the final TRUE contion (this is strange, but YEAH,.... that's it)
        def condition(mid,k):
            ## count number of elements in the matrix <= mid
            ## then we will know if cnt <= k
            ## if cnt >= k: r = mid
            ## if cnt < k: l = mid +1
            
            cnt = 0
            for i in range(1, m+1):
                addition = min(mid//i, n)        
                cnt += addition
                if addition ==0:
                    break
            return (cnt < k)
        
        while l<r:
            
            mid = l + (r-l)//2
            
            
            if condition(mid, k):
                l  = mid+1
            else:
                r = mid
                
        return l
                

        
            