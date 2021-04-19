'''
40. Combination Sum II

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
    def combinationSum2_slow_duplicated_res(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates = [tt for tt in candidates if tt<=target]
        if not candidates:
            return []
        
        dp = [ [] for _ in range(target + 1)]
        dp[0] = [ [0] ]
        ## must use reverse
        
        for c in candidates:
            for w in reversed(range(c, target+1)):
                if len(dp[w-c])>0:
                    dp_tmp = [ [tt for tt in ll] for ll in dp[w-c] ] 
                    for ll in dp_tmp:
                        ll.append(c)
                        
                    dp[w] += dp_tmp
                    
                    
        res = [ll[1:] for ll in dp[target] ]
        res_t = []
        for tt in res:
            tt.sort()
            tt = tuple(tt)
            if tt not in res_t:
                res_t.append(tt)
        print(res_t)
        if len(res_t) == 0 or len(res_t[0]) == 0:
            return []
        res = list(set(res_t))
        # print(res)
        return res
    
    def combinationSum2(self, candidates: List[int], target: int):
        candidates = [tt for tt in candidates if tt<=target]
        if len(candidates)==0:
            return []
        
        candidates.sort()
        
        dp = [ [] for _ in range(target + 1)]
        dp[0] = [ '0' ]
        ## must use reverse
        for c in candidates:
            for w in reversed(range(c, target+1)):
                if len(dp[w-c])>0:
                    
                    ## no need for extra space as
                    ## strings are immutable
                    # dp_tmp = [ tt for tt in dp[w-c] ] 
                    for ll in (dp[w-c]):
                        ll = '_'.join([ll,str(c)])
                        if ll not in dp[w]:
                            dp[w].append(ll)
                        
        res = [ll.split('_')[1:] for ll in dp[target] ]
        res = [[int(ss) for ss in ll] for ll in res if len(ll)>0]

        # if len(res) == 0 or len(res[0]) == 0: 
        #     return []

        return res
