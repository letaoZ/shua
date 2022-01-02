'''
485. Max Consecutive Ones
Easy

2137

391

Add to List

Share
Given a binary array nums, return the maximum number of consecutive 1's in the array.

 

Example 1:

Input: nums = [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.
Example 2:

Input: nums = [1,0,1,1,0,1]
Output: 2
 

Constraints:

1 <= nums.length <= 105
nums[i] is either 0 or 1.
'''

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ## solved generalized to k zeros
        ## also streaming the nums
        max_zero = 0
        queue_zero = collections.deque() ## allow k numbers in here and these are location of zero in the past
        idx = 0
        res = 0
        l = 0 ## left bound
        for n in nums:
            if n == 0:
                queue_zero.append(idx)
            if len(queue_zero)<=max_zero:
                pass
            else:
                
                l = queue_zero.popleft()
                l += 1
            res = max(res, idx - l + 1)
            idx += 1
            
        return res