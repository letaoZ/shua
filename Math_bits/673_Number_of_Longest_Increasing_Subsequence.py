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
class Solution1:
    ## fast with detailed analysis!
    
    def getIndex_left(self, nums, target):
        ## nums in descending, 
        ## find the index where to insert target
        ## if target == some elt in nums, find the smallest index to insert target
        
        l, r = 0, len(nums)
        if target >= nums[0]:
            return 0
        while l<r: # return r
            mid = l + (r-l) // 2
            
            if target> nums[mid]:
                r = mid
            elif target < nums[mid]:
                l = mid + 1
            elif target == nums[mid]:
                r = mid - 1
        return r
    def getIndex_right(self, nums, target):
        ## nums in descending, 
        ## find the index where to insert target
        ## if target == some elt in nums, find the largest index to insert target
        
        l, r = 0, len(nums)
        if target <= nums[-1]:
            return len(nums)
        
        while l<r: # return r
            mid = l + (r-l) // 2
            
            if target> nums[mid]:
                r = mid
            elif target < nums[mid]:
                l = mid + 1
            elif target == nums[mid]:
                l = mid + 1
        return r
    
    def findNumberOfLIS(self, nums: List[int]) -> int:
        ## pile_ends[pile_i] := the same as patience sorting, record each pile's ending element 
        ## piles[pile_i] := list of elts in each pile (each pile is decreasing, and the ending is the smallest)
        ## npahts[pile_i][j] := for pile pile_i, cummulative number of paths ending pile_i's jth elt. the cummulative is from the smallest (end of the pile) to that jth of the pile
        ## i.e. if a path can end with a small elt of pile_i, it can also end with anything that's larger than the smallest elt
        
        N = len(nums)
        if N <= 1:
            return N
        
        piles = [[nums[0]] ] # list of list
        piles_ends = [nums[0]]
        npaths = [[1]] ## following the same indexing as piles
        
        # print(self.getIndex_right([4],4))
        # return 0
        for i in range(1, N):
            elt = nums[i]
            # print(elt)
            # print(f"piles {piles}")
            # print(f"piles ends {piles_ends}")
            ## find which pile to put the elt in
            pile_i = bisect.bisect_left(piles_ends, elt)
            # print(f"pile i {pile_i}")
            if pile_i == len(piles): ## need a new pile
                piles.append([elt])
                piles_ends.append(elt)
                npaths.append([]) ## to be determined
            else:
                piles[pile_i].append(elt)
                piles_ends[pile_i] = elt
                
                
            ## if there is a pile before the elt's pile, find elts in previous pile that >= elt
            prev_paths = 0
            if pile_i-1 >= 0:
                prev_pos_elt = self.getIndex_right(piles[pile_i-1], elt) ## strictly increasing
                # print(f"prev_pos_elt {prev_pos_elt}")
                # print(f"prev pile {piles[pile_i-1]}")
                ## note: this elt cannot less than the smallest, otherwise it will be put into the previous pile
                ## the prev_pos_elt in previous pile and all elts after that are <= elt so we can have npaths[pile_i][prev_pos_elt] many paths to it
                prev_paths = npaths[pile_i-1][prev_pos_elt]
            else:
                prev_paths = 1 ## pile_i ==0
            
            ## now we need to see with in pile_i, the elt is the last one and it has prev_paths many connection.
            npaths[pile_i].append(prev_paths)
            
            ## update the cumsum of  previous index
            for pos in range(0,len(piles[pile_i])-1):
                npaths[pile_i][pos] += prev_paths
            # for ii in range(len(npaths)):
                # print(f"pile {ii} paths")
                # print(npaths[ii])
            # print()
            
        
        return npaths[-1][0]
            
                

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
    
    def findNumberOfLIS_2d(self, nums: List[int]) -> int:
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