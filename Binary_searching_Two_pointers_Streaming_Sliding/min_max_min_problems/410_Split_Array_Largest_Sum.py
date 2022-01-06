'''
410. Split Array Largest Sum
Hard

3928

121

Add to List

Share
Given an array nums which consists of non-negative integers and an integer m, you can split the array into m non-empty continuous subarrays.

Write an algorithm to minimize the largest sum among these m subarrays.

 

Example 1:

Input: nums = [7,2,5,10,8], m = 2
Output: 18
Explanation:
There are four ways to split nums into two subarrays.
The best way is to split it into [7,2,5] and [10,8],
where the largest sum among the two subarrays is only 18.
Example 2:

Input: nums = [1,2,3,4,5], m = 2
Output: 9
Example 3:

Input: nums = [1,4,4], m = 3
Output: 4
 

Constraints:

1 <= nums.length <= 1000
0 <= nums[i] <= 106
1 <= m <= min(50, nums.length)
'''


class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        ## splitArray_left_closed_right_open
        ## largest sum is at least max(nums) as the max must be in a pile
        ## NOTE: the left end MUST be achievable for this to work!
        l, r = max(nums), sum(nums)+1
        ## [l, r), return l
        while l< r:
            mid = l + (r-l) // 2
            # print("l: ", l)
            # print("mid: ", mid)

            tmp = 0
            cnt = 0
            for i in range(len(nums)):
                if tmp + nums[i] > mid:
                    cnt += 1
                    tmp = nums[i]
                elif tmp + nums[i] <= mid:
                    tmp += nums[i]
            cnt += 1 ## the last tmp has to be added anyways!
            
            
            # print("cnt: ", cnt)
            # print("res: ", res)
            # print()
            if cnt == m: ## we maybe able to lower the right bound
                r = mid
            elif cnt < m: ## we can make more cnt by decreases the max: so lower the right bound, to make more cnt
                r = mid
            elif cnt > m:
                l = mid + 1
                
            elif cnt <= m:
                r = mid
                
        
                
        return l

    