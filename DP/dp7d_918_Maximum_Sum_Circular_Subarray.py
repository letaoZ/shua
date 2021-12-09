'''
918. Maximum Sum Circular Subarray
Medium

2442

102

Add to List

Share
Given a circular integer array nums of length n, return the maximum possible sum of a non-empty subarray of nums.

A circular array means the end of the array connects to the beginning of the array. Formally, the next element of nums[i] is nums[(i + 1) % n] and the previous element of nums[i] is nums[(i - 1 + n) % n].

A subarray may only include each element of the fixed buffer nums at most once. Formally, for a subarray nums[i], nums[i + 1], ..., nums[j], there does not exist i <= k1, k2 <= j with k1 % n == k2 % n.

 

Example 1:

Input: nums = [1,-2,3,-2]
Output: 3
Explanation: Subarray [3] has maximum sum 3
Example 2:

Input: nums = [5,-3,5]
Output: 10
Explanation: Subarray [5,5] has maximum sum 5 + 5 = 10
Example 3:

Input: nums = [3,-1,2,-1]
Output: 4
Explanation: Subarray [2,-1,3] has maximum sum 2 + (-1) + 3 = 4
Example 4:

Input: nums = [3,-2,2,-3]
Output: 3
Explanation: Subarray [3] and [3,-2,2] both have maximum sum 3
Example 5:

Input: nums = [-2,-3,-1]
Output: -1
Explanation: Subarray [-1] has maximum sum -1
 

Constraints:

n == nums.length
1 <= n <= 3 * 104
-3 * 104 <= nums[i] <= 3 * 104
Accepted
92,529
Submissions
257,815

'''
class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        
        ## psum[i]:= all possible sums sum(nums[:(i)]) if i<N else sum(nums + sum(nums[:i]))
        
        N = len(nums)
        psum = [0]*(N + 1)
        for i in range(1,N+1):
            psum[i] = psum[i-1] + nums[(i-1)]
            
            
            
            
            
        N = len(psum)
        l, r = 0, 0
        
        cur_min_left = 0
        res = max(nums)

        while l<N-1:
            while l<N-1 and psum[l]>psum[l+1]:
                l += 1
            r = l+1
            while r<N-1 and psum[r]<=psum[r+1]:
                r += 1
            if r>=N:
                break
            cur_min_left = min(cur_min_left, psum[l])
            res = max(res, psum[r] - cur_min_left)     
            l = r + 1
        
        ## psum again, but we compare right sum and left sum, both max
        print("res",res)
        

        l, r = 0, 0
        cur_max_left = -float('inf')
        while l<N-1:
            while l<N-1 and psum[l]<=psum[l+1]:
                l += 1
            ## reached left part max
            r = l+1
            while r<N-1 and psum[r]>=psum[r+1]:
                r += 1
            if r>=N-1:
                break
            ## when psum[r] reaches smallest, it means the right sum reach the max
            cur_max_left = max(cur_max_left, psum[l])
            r_sum = psum[N-1] - psum[r]
            
            res = max(res, r_sum + cur_max_left)
            l = r+1
        return res
        