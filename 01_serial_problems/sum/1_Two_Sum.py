'''
1. Two Sum
Easy


Share
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
 

Constraints:

2 <= nums.length <= 103
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.
'''


class Solution:
    def twoSum_basic(self,nums, target):

        
        for i,v in enumerate(nums):
            target_v = target - v
            if target_v in nums[:i]+nums[i+1:]:
                k = nums.index(target_v)
                if target_v!=v or k!=i:
                    return [i,k]
                else:
                    k = k+1+nums[k+1:].index(target-v)

                    return [i,k]

        return [-1,-1]

    def twoSum_dict(self,nums, target):
        

        ## keep track of visited indices 
        ## whose values could be future's: target - v
        res = {}
        for i,v in enumerate(nums):
            target_v = target - v
            if target_v in res:
                return [res[target_v],i]
            else:
                res[v] = i

        return [-1,-1]
    def twoSum(self,nums, target):

        ## use binary search
        nums = [ [n,i] for i,n in enumerate(nums)]
        nums.sort(key = lambda kv:(kv[0], kv[1]))

        l = 0
        r = len(nums) - 1

        while l<r:
            nl = nums[l][0]
            target_v = target - nl
            if target_v > nums[r][0]:
                l += 1
            elif target_v == nums[r][0]:
                return [nums[l][1],nums[r][1]]
            else:
                r -= 1
            print(nums[l][0],nums[r][0])
        return [-1,-1]
            



nums = [2,11,2,15]
target = 4
solu = Solution()

solu.twoSum(nums,target)

