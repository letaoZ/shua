'''
90. Subsets II
Medium

4165

134

Add to List

Share
Given an integer array nums that may contain duplicates, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

 

Example 1:

Input: nums = [1,2,2]
Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
Example 2:

Input: nums = [0]
Output: [[],[0]]
 

Constraints:

1 <= nums.length <= 10
-10 <= nums[i] <= 10
'''

class Solution:
    def subsetsWithDup_simplify(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        def dfs(i, trace, nums,  res):
            
            if trace not in res:
                res.append([_ for _ in trace])
            
            if i == len(nums):
                return
            
            for j in range(i,len(nums)):
                dfs(j+1, trace + [nums[j]], nums, res)
                
        dfs(0, [], nums, res)
        return res
    
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = set()
        nums.sort() ## use sort to avoid future duplicates
        def dfs(nums,i,trace):
            
            # new_trace = [_ for _ in trace]
            # new_trace.sort()
            res.add(tuple(trace))
            # del new_trace
            
            
            if i >= len(nums):
                return
            
            
            for j in range(i,len(nums)):
                trace.append(nums[j])
                dfs(nums,j+1,trace)
                trace.pop()
                
        dfs(nums,0,[])        
        res = [list(_) for _ in res]
        
        return res
                
                