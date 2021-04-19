'''
377. Combination Sum IV
Medium

Given an array of distinct integers nums and a target integer target, 
return the number of possible combinations that add up to target.

The answer is guaranteed to fit in a 32-bit integer.

 

Example 1:

Input: nums = [1,2,3], target = 4
Output: 7
Explanation:
The possible combination ways are:
(1, 1, 1, 1)
(1, 1, 2)
(1, 2, 1)
(1, 3)
(2, 1, 1)
(2, 2)
(3, 1)
Note that different sequences are counted as different combinations.
Example 2:

Input: nums = [9], target = 3
Output: 0
 

Constraints:

1 <= nums.length <= 200
1 <= nums[i] <= 1000
All the elements of nums are unique.
1 <= target <= 1000
 

Follow up: What if negative numbers  are allowed in the given array? 
How does it change the problem? 
What limitation we need to add to the question to allow negative numbers?

'''


## Extra question
## if negative numbers are allow, then you may have infinitly many solutions
## say -1 and 1 both in the set, then you get zeros. so if you don't enforce 
## each number being used at most once, then you get infinitely many solutions
## constraints could be: no combination = 0
class Solution:
    def combinationSum4_knapsack(self, nums: List[int], target: int) -> int:
        ##knapsack
        
        min_n = min(nums)
        if min_n > target:
            return 0
        if min_n == target:
            return 1
        nums = [ss for ss in nums if ss <= target]
        nums.sort()
        
        sz = len(nums)
        
        ## to get target kk, number of ways
        dp = [0 for _ in range(target+1)] 
        dp[0] = 1
        
   
        for tar in range(1,target+1):
            for num in nums:
                if num > tar: break
                else:
                    dp[tar] += dp[tar-num]
                    
        return (dp[-1])
    def combinationSum4(self, nums: List[int], target: int) -> int:
        
        ## number of ways to get w
        
        min_n = min(nums)
        if min_n > target:
            return 0
        if min_n == target:
            return 1
        
        nums.sort()
        dp = [ -1 for _ in range(target+1)]
        dp[0] = 1
        
        def searching(nums, tar, dp):
            if tar <0:
                return 0

            if dp[tar]!=-1:
                return dp[tar]
            dp[tar] = 0
            for nn in nums:
                dp[tar] += searching(nums, tar-nn, dp)
            return dp[tar]
        
        
        return searching(nums, target, dp)