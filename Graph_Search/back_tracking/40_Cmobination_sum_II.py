'''
40. Combination Sum II
Medium

4325

121

Add to List

Share
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.

Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.

 

Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8
Output: 
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]
Example 2:

Input: candidates = [2,5,2,1,2], target = 5
Output: 
[
[1,2,2],
[5]
]
 

Constraints:

1 <= candidates.length <= 100
1 <= candidates[i] <= 50
1 <= target <= 30

'''


class Solution:
    def combinationSum2_knapsack(self, candidates: List[int], target: int) -> List[List[int]]:
        
        ## knapsack
        ## dp[s] := collection numbers that sum to s
        dp = collections.defaultdict(list) 
        dp[0] = [()]
        candidates.sort()
        for c in candidates:
            for s in range(target, c-1,-1):
                for l in dp[s-c]:
                    new_t = tuple(list(l) + [c])
                    if new_t not in dp[s]:
                        dp[s].append(new_t)
                
        res = list(list(_) for _ in dp[target])
        # res = list(list(_) for _ in res)
        return res
    
    def combinationSum2_backtracking(self, candidates: List[int], target: int) -> List[List[int]]:
        ## treet structure: Time O(2^N )
        res = []
        candidates.sort()

        def dfs(i, candidates, trace, cur_sum, target):
            if cur_sum == target:
                t = tuple(trace)
                if t not in res:
                    res.append(t)
                    
                return
            if cur_sum > target:
                return
            if i>= len(candidates):
                return
            
            for j in range(i,len(candidates)):
                if j>i and (candidates[j] == candidates[j-1]):## important step!!
                    continue
                trace.append(candidates[j])
                dfs(j+1, candidates,trace, cur_sum + candidates[j], target)
                trace.pop()
                
                
        dfs(0, candidates, [], 0, target)
        res = [list(_) for _ in res]
        return res