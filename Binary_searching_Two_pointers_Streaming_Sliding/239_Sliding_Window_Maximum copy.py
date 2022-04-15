'''
239. Sliding Window Maximum
Hard

9455

334

Add to List

Share
You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

Return the max sliding window.

 

Example 1:

Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
Explanation: 
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
Example 2:

Input: nums = [1], k = 1
Output: [1]
 

Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
1 <= k <= nums.length'''

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        ## assume len(nums) >0, k>0
        
        
        
        res = [0] * len(nums)
        
        window = collections.deque() ## first elt of window is cur_max of form (elt, idx)
        for i in range(0, len(nums)):
            num = nums[i]
            
            ## window: nonincreasing
            while window and num>window[-1][0]:
                window.pop()
            window.append((num,i))
            
            ## remove expired elt
            ## for each idx, furthest it reaches is idx + k - 1
            while window and window[0][1]+k-1<i:
                window.popleft()
                
            res[i] = window[0][0]
                
        return res[k-1:]
            
            