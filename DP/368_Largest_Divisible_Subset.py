'''
368. Largest Divisible Subset
Medium

2924

135

Add to List

Share
Given a set of distinct positive integers nums, return the largest subset answer such that every pair (answer[i], answer[j]) of elements in this subset satisfies:

answer[i] % answer[j] == 0, or
answer[j] % answer[i] == 0
If there are multiple solutions, return any of them.

 

Example 1:

Input: nums = [1,2,3]
Output: [1,2]
Explanation: [1,3] is also accepted.
Example 2:

Input: nums = [1,2,4,8]
Output: [1,2,4,8]
 

Constraints:

1 <= nums.length <= 1000
1 <= nums[i] <= 2 * 109
All the integers in nums are unique.
'''

class Solution:
    def largestDivisibleSubset_memory_overflow(self, nums: List[int]) -> List[int]:
        nums.sort()
        ## dp[k] := longest including nums[k], in nums[..k]
        ## Memory Limit Exceeded
        dp = [1]*(len(nums))
        cnt = collections.defaultdict(list)
        cnt[0] = [ [nums[0]] ] ## including nums[k], cnt[k] list of sequence of longest length dp[k] including k
        res = 1 ## max len
        for k in range(1, len(nums)):
            cur_max = 1
            for j in range(k):
                
                if nums[k] % nums[j] == 0:
                    if dp[j] + 1 > cur_max:
                        dp[k] = dp[j] + 1
                        cnt[k] = []
                        cur_max = dp[k]
                    if dp[j] + 1  == cur_max:
                        for l in cnt[j]:
                            cnt[k].append(l+[nums[k]] ) 
            if cur_max == 1:
                cnt[k] = [ [nums[k]]]
            res = max(res,dp[k]) ## max len
            cur_max = res
            
        # print(cnt)
        for i,l in enumerate(dp):
            if l == res:
                return cnt[i][0]
            
        return res
    
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        ## dp[k] := longest including nums[k], in nums[..k]
        ## Memory Limit Exceeded
        dp = [1]*(len(nums))
        cnt = collections.defaultdict(list)
        cnt[0] = [] ## including nums[k], cnt[k] list of node index (right before k) of longest length dp[k] including k
        res = 1 ## max len
        for k in range(1, len(nums)):
            cur_max = 1
            # print("k: ",k)
            # print(nums[k])
            for j in range(k):
                
                if nums[k] % nums[j] == 0:
                    if dp[j] + 1 > cur_max:
                        dp[k] = dp[j] + 1
                        cnt[k] = []
                        cur_max = dp[k]
                    if dp[j] + 1  == cur_max:
                        cnt[k].append(j)

            res = max(res,dp[k]) ## max len
            

        for i,l in enumerate(dp):
            if l == res:
                ## find the result one by one till we reach length l
                ans = [0]*l
                ans[l-1] = nums[i]
                l -= 1
                while l:
                    i = cnt[i][0]
                    ans[l-1] = nums[i]
                    l -= 1
        return ans
            