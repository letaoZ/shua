'''
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

 

Example 1:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
Example 2:

Input: nums = [0,1]
Output: [[0,1],[1,0]]
Example 3:

Input: nums = [1]
Output: [[1]]
 

Constraints:

1 <= nums.length <= 6
-10 <= nums[i] <= 10
All the integers of nums are unique.
'''

class Solution:
    def permute0(self, nums: List[int]) -> List[List[int]]:
        ## dfs: backtracking
        res = []
        n = len(nums)
        visited = [0]*n ## index i is visited or not
        def dfs(trace,visited,res):
            if len(trace) == n:
                res.append([_ for _ in trace])
                return
            
            for i in range(n):
                if visited[i]:
                    continue
                    
                trace.append(nums[i])
                visited[i] = 1
                dfs(trace,visited,res)
                trace.pop()
                visited[i] = 0
                
                
        dfs([],visited,res)
        return (res)
    
    
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        
        ##
        
        res = []
        n = len(nums)
        candidate = [_ for _ in range(n)] ## candidate: index of numbers left to be put into a permutation
        
        def dfs(trace,candidate,res):
            if len(trace) == n:
                res.append([_ for _ in trace]) ## make a new copy
                return
            
            for ic,v in enumerate(candidate):
                    
                trace.append(nums[v])
                dfs(trace,candidate[:ic]+candidate[ic+1:],res)
                trace.pop()
                
                
        dfs([],candidate,res)
        return (res)
