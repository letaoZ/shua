'''
974. Subarray Sums Divisible by K
Medium

Given an array A of integers, return the number of (contiguous, non-empty) subarrays that have a sum divisible by K.

Example 1:

Input: A = [4,5,0,-2,-3,1], K = 5
Output: 7
Explanation: There are 7 subarrays with a sum divisible by K = 5:
[4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2, -3]
 

Note:

1 <= A.length <= 30000
-10000 <= A[i] <= 10000
2 <= K <= 10000
'''

import collections
class Solution:
    def subarraysDivByK(self, A, K) -> int:


        A = [tt%K for tt in A]
        dp = collections.defaultdict(int)

        dp[0] = 1
        cur_sum = 0
        res = 0
        for n in A:
            cur_sum += n
            cur_sum  = cur_sum%K
            res += dp[cur_sum]
            dp[cur_sum] += 1
            
        return res

A = [1,4,1,2,2,3]
K = 5
solu = Solution()
solu.subarraysDivByK(A,K)