'''
673. Number of Longest Increasing Subsequence
Medium

3024

149

Add to List

Share
Given an integer array nums, return the number of longest increasing subsequences.

Notice that the sequence has to be strictly increasing.

 

Example 1:

Input: nums = [1,3,5,4,7]
Output: 2
Explanation: The two longest increasing subsequences are [1, 3, 4, 7] and [1, 3, 5, 7].
Example 2:

Input: nums = [2,2,2,2,2]
Output: 5
Explanation: The length of longest continuous increasing subsequence is 1, and there are 5 subsequences' length is 1, so output 5.

 

Constraints:

1 <= nums.length <= 2000
-106 <= nums[i] <= 106
'''

class Solution:
    def findNumberOfLIS_slow(self, nums: List[int]) -> int:
        ## dp[k][l] := including nums[k], in nums[..k],  num of increasing subsequence of length l
        ## for each length record num of sequence as well
        
        
        
        dp = [[0]*(len(nums)+1) for _ in range(len(nums))]
        for k in range(0,len(nums)):
            dp[k][1] = 1
        # dp[0][0] = 1
        max_len = 1
        
        ## time= O(N^3)
        for k in range(1,len(nums)):
            ## nums[0,1]
            for i in range(k):
                if nums[k] > nums[i]:
                    for l in range(1,len(nums)):
                        dp[k][l+1] += dp[i][l]
                        if dp[k][l+1]>0:
                            max_len = max(max_len, l+1)
        #     print(k)
        #     print(dp[k])
        #     print()
        # print(max_len)

        return (sum([dp[k][max_len] for k in range(len(nums))]))
    
    def findNumberOfLIS_square_speed(self, nums: List[int]) -> int:
        """
        :type nums: List[int]
        :rtype: int
        """
        # Time: O(n^2)
        # Space: O(n)
        # dp[j][0] := length of longest subseq ending at j
        # dp[j][1] := number of subseq ending at j that have the longest length
        dp, longest = [[1, 1] for i in range(len(nums))], 1
        
        for i, num in enumerate(nums):
            curr_longest, count = 1, 0
            for j in range(i):
                if nums[j] < num:
                    curr_longest = max(curr_longest, dp[j][0] + 1)
                    ## first find the longest length
            for j in range(i):
                if dp[j][0] == curr_longest - 1 and nums[j] < num:
                    count += dp[j][1]
            dp[i] = [curr_longest, max(count, 1)]
            longest = max(curr_longest, longest)
        return sum([item[1] for item in dp if item[0] == longest])
    
    def findNumberOfLIS(self, nums: List[int]) -> int:
        # dp[j][0] := length of longest subseq ending at j
        # dp[j][1] := number of subseq ending at j that have the longest length
        dp = [ [1,1] for _ in range(len(nums))]
        
        max_len = 1
        
        for i in range(1,len(nums)):
            cur_max_len = 1
            cur_max_cnt = 0
            for j in range(i):
                if nums[j]<nums[i]:
                    if dp[j][0] + 1 > cur_max_len:
                        cur_max_cnt = 0
                        cur_max_len = dp[j][0] + 1
                        
                    if cur_max_len == dp[j][0] + 1:
                        
                        cur_max_cnt += dp[j][1]
                        
            max_len = max(max_len, cur_max_len)
            dp[i] = [cur_max_len, max(cur_max_cnt,1)]
        # print(max_len)
        # print(dp)
        return sum([dp[j][1] for j in range(len(nums)) if dp[j][0] == max_len])