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

## idea: maintain a relative order of nums: e.g. [1,2,2,2], then assume the "2nd" 2 is actually 2'. 3rd 2 is 2''
## Then we must maintain 2' showup before 2'' and 2 shows up before 2' -- > SO we wont' get duplicate cases
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        visited = [0]*len(nums)
        def dfs(nums,trace,res):
            
            if len(trace) == len(nums):
                res.append([_ for _ in trace])
                return
            
            for j in range(0, len(nums)):
                if visited[j]:
                    continue
                if j>0 and nums[j] == nums[j-1] and (not visited[j-1]):
                    continue
                visited[j] = 1
                dfs(nums, trace + [nums[j]],res)
                visited[j] = 0
                
        dfs(nums,[],res)
                
        return res
            

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
                