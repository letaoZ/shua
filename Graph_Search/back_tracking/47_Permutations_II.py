'''
47. Permutations II
Medium

4288

88

Add to List

Share
Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.

 

Example 1:

Input: nums = [1,1,2]
Output:
[[1,1,2],
 [1,2,1],
 [2,1,1]]
Example 2:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
 

Constraints:

1 <= nums.length <= 8
-10 <= nums[i] <= 10
'''


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = set()
        N = len(nums)
        def dfs(candidates, trace):
            
            if len(trace) == N:
                res.add(tuple([_ for _ in trace]))
                return
            
            
            for ic, v in enumerate(candidates):
                trace.append(v)
                dfs(candidates[:ic] + candidates[ic+1:], trace)
                trace.pop()
                
                
        dfs(nums, [])
        res = [list(_) for _ in res]
                
        return res
                