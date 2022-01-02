'''
487. Max Consecutive Ones II
Medium

954

17

Add to List

Share
Given a binary array nums, return the maximum number of consecutive 1's in the array if you can flip at most one 0.

 

Example 1:

Input: nums = [1,0,1,1,0]
Output: 4
Explanation: Flip the first zero will get the maximum number of consecutive 1s. After flipping, the maximum number of consecutive 1s is 4.
Example 2:

Input: nums = [1,0,1,1,0,1]
Output: 4
 

Constraints:

1 <= nums.length <= 105
nums[i] is either 0 or 1.
 

Follow up: What if the input numbers come in one by one as an infinite stream? In other words, you can't store all numbers coming from the stream as it's too large to hold in memory. Could you solve it efficiently?
'''



class Solution:
    def findMaxConsecutiveOnes_long_solut(self, nums: List[int]) -> int:
        ## dp[k] := num of consecutive ones in nums[:k] including nums[k]
        ## latest_one index: index of the beginning of the latest conseq ones
        N = len(nums)
        
        if N == 1:
            return 1
        dp = [0]*(N+1) ## cushion dp[N] using as dp[-1], if nums start with 0, we assume last_one as -1, i.e. dp[-1] is zero to allow dp[i] +d[-1] + 1
        dp[0] = nums[0]
        last_one = -2 ## zero never showed up
        latest_one= -1
        if nums[0] == 1:
            latest_one = 0
        if nums[0] == 0:
            last_one = -1
        res = 1
        for i in range(1,N):
            # print(latest_one)
            # print(last_one)
            if nums[i] == 0:
                if nums[i-1] == 1:
                    last_one = i-1 ## potential to glue
                    res = max(res,dp[last_one] + 1)
                else:
                    last_one = -1 ## two consective zeros, you cannot glue 
            elif nums[i] == 1:
                if nums[i-1] == 0:
                    latest_one = i
                dp[i] = i-latest_one+1
                res = max(dp[i],res)
                if last_one != -2:## last_one == -2 means we never seen 10
                    res = max(res,dp[i] + dp[last_one] + 1)
            # print(dp)
            # print()
        return res
    def findMaxConsecutiveOnes_simplified_long(self, nums: List[int]) -> int:
        ## onetime count num of ones before zero
        ## two time count glud conseq sum
        res = 0
        twotime = 0
        onetime = 0
        for num in nums:
            if (num == 0):
                twotime = onetime + 1
                onetime = 0
            else:
                onetime += 1
                twotime += 1
                
            res = max(res, twotime)
        return res
        
        
    def findMaxConsecutiveOnes_generalize_k_zeros(self, nums: List[int]) -> int:
        ## l := left most starting point
        ## r := right most reached point
        ## for each farthest reached point (including it), max we can get
        max_zero = 1 ## max num of zeros allowed
        zeros = 0 ## currently num of zeros used
        l = 0
        res = 0
        for r in range(len(nums)):
            n = nums[r]
            if n == 0:
                zeros += 1
            if zeros <= max_zero:
                ## good
                # print("d")
                pass
            else:## if allowed zeros > max_zeros; we shift left to the most recent allowed 1 or 0
                while zeros > max_zero:
                    if nums[l] == 0:
                        zeros -= 1
                    
                    l += 1
                    
            res = max(res, r - l + 1)
        return res
    
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ## solved generalized to k zeros
        ## also streaming the nums
        max_zero = 1
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
        
        