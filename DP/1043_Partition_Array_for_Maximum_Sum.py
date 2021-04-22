'''
1043. Partition Array for Maximum Sum
Medium

Given an integer array arr, you should partition the array into (contiguous) subarrays of length at most k. After partitioning, each subarray has their values changed to become the maximum value of that subarray.

Return the largest sum of the given array after partitioning.

 

Example 1:

Input: arr = [1,15,7,9,2,5,10], k = 3
Output: 84
Explanation: arr becomes [15,15,15,9,10,10,10]
Example 2:

Input: arr = [1,4,1,5,7,3,6,1,9,9,3], k = 4
Output: 83
Example 3:

Input: arr = [1], k = 1
Output: 1
 

Constraints:

1 <= arr.length <= 500
0 <= arr[i] <= 109
1 <= k <= arr.length
'''

class Solution:
    def maxSumAfterPartitioning_dp_wo_store_psum(self, A: List[int], K: int) -> int:
        if K == 1: return sum(A)
        if K>=len(A): return max(A)*len(A)
           
        ## dp[i] -- max sum you can get using the first i elts
        dp = [0]*(len(A)+1)
        for i in range(1,len(A)+1):       
            m = 0
            for dist_to_i in range(1,K+1):
                if i - dist_to_i<0: break
                m = max(m, A[i - dist_to_i]);
                dp[i] = max(dp[i], dp[i - dist_to_i] + m * dist_to_i)
                
        
        
        return dp[-1]

    def maxSumAfterPartitioning_dp_recur_store_ij(self, A: List[int], K: int) -> int:
        if K == 1: return sum(A)
        if K>=len(A): return max(A)*len(A)
        
        ## min number of sets
        N = len(A)//K
        if N*K!=len(A):
            N += 1
        
        dp = [[-1]*len(A) for _ in range(len(A))] ## from ith to jth elt inclusive max sum
        
        
        for i in range(len(A)):
            dp[i][i] = A[i]
            
        def searching(A,i,j):
            if i == j:
                return A[i]
            if i>j:
                return 0
            if dp[i][j]>-1:
                return dp[i][j]

            for a in range(i,j+1):
                sz = a-i+1
                if sz>K: break
                psum = amax[i][a]*sz#max(A[i:a+1])*sz
                dp[i][j] = max(dp[i][j],psum + searching(A,a+1,j))
            return dp[i][j]
        
        searching(A,0,len(A)-1)
        
        return dp[0][len(A)-1]
                
        

    def maxSumAfterPartitioning_brutal_recurr_store_all_sum(self, A: List[int], K: int) -> int:
        if K == 1: return sum(A)
        if K>=len(A): return max(A)*len(A)
        
        ## min number of sets
        N = len(A)//K
        if N*K!=len(A):
            N += 1
            
        def searching(nums,res,res_list):
            if len(nums)==0:
                res_list.append(res)
                return
            
            for i in range(1,min(K+1,len(nums)+1)):
                psum = max(nums[:i])*i
                searching(nums[i:],res+psum,res_list)
        res = 0
        res_list = []
        searching(A,res,res_list)
        
        return max(res_list)
                
        