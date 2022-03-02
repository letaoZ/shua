'''300. Longest Increasing Subsequence
Medium

9877

201

Add to List

Share
Given an integer array nums, return the length of the longest strictly increasing subsequence.

A subsequence is a sequence that can be derived from an array by deleting some or no elements without changing the order of the remaining elements. For example, [3,6,2,7] is a subsequence of the array [0,3,1,6,2,2,7].

 

Example 1:

Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
Example 2:

Input: nums = [0,1,0,3,2,3]
Output: 4
Example 3:

Input: nums = [7,7,7,7,7,7,7]
Output: 1
 

Constraints:

1 <= nums.length <= 2500
-104 <= nums[i] <= 104
'''



class Solution:
    def lengthOfLIS_dp(self, nums: List[int]) -> int:
      
        ## dp[i] := longest increasing seq including nums[i]
        N = len(nums)
        dp = [1]*N
        res = 0
        for i in range(0,N):
            for j in range(i):
                if nums[i]>nums[j]:
                    dp[i] = max(dp[i],dp[j] + 1)
            res = max(res,dp[i])
        return res
        
    def lengthOfLIS_patience_sort(self, nums: List[int]) -> int:
        ## patience sort
        ## define a game: draw card from nums one by one
        ## form new piles from cards, each pile is non-increasing
        ## we form new piles greedily, only start a new pile when you cannot add card to existing ones
        ## theorem: min number of piles == max length of an increasing sequence in nums
        
        piles = []
        N = len(nums)
        for i in range(N):
            l = len(piles)
            for k in range(len(piles)):
                if nums[i]<=piles[k]:
                    piles[k] = nums[i]
                    l = k
                    break
            if l == len(piles):
                piles.append(nums[i]) ## starting a new pile
                
        return len(piles)
        
    # def lengthOfLIS_patience_sort_with_bs(self, nums: List[int]) -> int:
    def lengthOfLIS(self, nums: List[int]) -> int:

        ## patience sort
        ## define a game: draw card from nums one by one
        ## form new piles from cards, each pile is non-increasing
        ## we form new piles greedily, only start a new pile when you cannot add card to existing ones
        ## theorem: min number of piles == max length of an increasing sequence in nums
        
        piles = []
        N = len(nums)
        for i in range(N):
            ## instead of loop through all exisiting elts in piles 
            ## we run binary search to find location
            
            num = nums[i]
            l, r = 0, len(piles) ## return l
            # print(num)
            while l<r:
                mid = l + (r-l) // 2
                if piles[mid]< num:
                    l = mid + 1
                elif piles[mid]>num:
                    r = mid
                elif piles[mid] == num:
                    l = mid
                    break
            # print(l)
            # print(piles)
            if l == len(piles):
                piles.append(nums[i]) ## starting a new pile
            else:
                piles[l] = num
            # print(piles)
            # print()
        # print(piles)
        return len(piles)
            
            