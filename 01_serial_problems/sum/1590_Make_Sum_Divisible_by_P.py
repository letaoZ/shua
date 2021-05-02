'''
1590. Make Sum Divisible by P
Medium

Given an array of positive integers nums, remove the smallest subarray (possibly empty) such that the sum of the remaining elements is divisible by p. It is not allowed to remove the whole array.

Return the length of the smallest subarray that you need to remove, or -1 if it's impossible.

A subarray is defined as a contiguous block of elements in the array.

 

Example 1:

Input: nums = [3,1,4,2], p = 6
Output: 1
Explanation: The sum of the elements in nums is 10, which is not divisible by 6. We can remove the subarray [4], and the sum of the remaining elements is 6, which is divisible by 6.
Example 2:

Input: nums = [6,3,5,2], p = 9
Output: 2
Explanation: We cannot remove a single element to get a sum divisible by 9. The best way is to remove the subarray [5,2], leaving us with [6,3] with sum 9.
Example 3:

Input: nums = [1,2,3], p = 3
Output: 0
Explanation: Here the sum is 6. which is already divisible by 3. Thus we do not need to remove anything.
Example 4:

Input: nums = [1,2,3], p = 7
Output: -1
Explanation: There is no way to remove a subarray in order to get a sum divisible by 7.
Example 5:

Input: nums = [1000000000,1000000000,1000000000], p = 3
Output: 0
 

Constraints:

1 <= nums.length <= 105
1 <= nums[i] <= 109
1 <= p <= 109


'''



class Solution:
    def minSubarray_memo_slow(self, nums:  [int], p: int) -> int:
        
        
        nums = [tt%p for tt in nums]
        
        if p==1:
            return 0
    
        r = (sum(nums))   
        if r<p:
            return -1
        
        r = (r%p)
        if r == 0:
            return 0
        
        ## if after removing subarray psum, the rest is divisible by p
        ## then (Total - psum)%p == 0
        ## Thus, psum%p == Total%p
        
        sz = len(nums)
        ## dp[j]: sum of nums[:j]
        dp = [0]*(1+sz)
        for i in range(1,sz+1):
            dp[i] = (dp[i-1]+nums[i-1])%p
            
        
        ## brutal force
        for l in range(1,sz):
            for i in range(0,sz-l+1):
                if (dp[i+l] - dp[i])%p == r: 
                    return l
                
        return -1 
    
    def minSubarray(self, nums:  [int], p: int) -> int:
        
        nums = [tt%p for tt in nums]
        
        if p==1:
            return 0
    
        r = sum(nums)
        r = (r%p)
        if r == 0:
            return 0
        
        if r in nums:
            return 1
        
        ## if after removing subarray psum, the rest is divisible by p
        ## then (Total - psum)%p == 0
        ## Thus, psum%p == r

        
        psum = {0:-1}
        cur = 0
        ans = len(nums)
        for i, n in enumerate(nums):
            cur += n
            cur %= p
            reminder = (cur-r)%p
            if reminder in psum:
                ans = min(ans, i-psum[reminder])
            
            psum[cur] = i

        return ans if ans<len(nums) else -1



solu = Solution()

nums = [1,2,3]
p = 2
solu.minSubarray(nums, p)