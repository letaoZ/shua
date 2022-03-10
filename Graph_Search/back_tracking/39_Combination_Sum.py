'''
39. Combination Sum
## knapsack or backtracking--DFS

Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.

It is guaranteed that the number of unique combinations that sum up to target is less than 150 combinations for the given input.

 

Example 1:

Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.
Example 2:

Input: candidates = [2,3,5], target = 8
Output: [[2,2,2,2],[2,3,3],[3,5]]
Example 3:

Input: candidates = [2], target = 1
Output: []
 

Constraints:

1 <= candidates.length <= 30
1 <= candidates[i] <= 200
All elements of candidates are distinct.
1 <= target <= 500
'''


class Solution:
    
    def combinationSum_knapsack(self, candidates: List[int], target: int) -> List[List[int]]:
        ## space = O(target**2)
        ## time = O(len(candidtes)*target)
        ## for each sum, keep track combinations reaching that sum
        
        traces = collections.defaultdict(list)

        traces[0].append([])
        for c in candidates:
            for wt in range(c,target+1):
                if traces[wt-c]:
                    for l in traces[wt-c]:
                        traces[wt].append(l + [c])
        if traces[target] == [[]]:
            return []
        return traces[target]
        # since target >= 1, we don't need the following step
        # if len(res) == 0 or len(res[0]) == 0:
        #     return []
        
                

        
    def combinationSum_backtracking(self, candidates: List[int], target: int) -> List[List[int]]:
        ## backtracking = dfs
        ## edges = len(candidates)**2
        ## nodes = len(candidates)*target (since each node can be used more than once)
        
        res = []
        
        def dfs(i,target,trace,cur_sum,res):
            if cur_sum == target:
                res.append([_ for _ in trace])
                return
            if cur_sum > target:
                return
            
            for i in range(i, len(candidates)):
                c = candidates[i]
                trace.append(c)
                dfs(i, target,trace,cur_sum+c,res )
                trace.remove(c)
        dfs(0, target,[],0,res)
        return res
    
    
    def combinationSum_backtracking_shorten(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        def dfs(i,target,trace, candidates, res):
            
            if target<0:
                return
            if target == 0:
                res.append([_ for _ in trace])
                return
            
            for j in range(i,len(candidates)):
                dfs(j, target - candidates[j], trace + [candidates[j]], candidates, res)
                
        dfs(0,target, [], candidates, res)
        return res