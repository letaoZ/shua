'''
1004. Max Consecutive Ones III
Medium

3614

50

Add to List

Share
Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

 

Example 1:

Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
Output: 6
Explanation: [1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
Example 2:

Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
Output: 10
Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
 

Constraints:

1 <= nums.length <= 105
nums[i] is either 0 or 1.
0 <= k <= nums.length
'''

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        ## solved generalized to k zeros
        ## also streaming the nums
        max_zero = k
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