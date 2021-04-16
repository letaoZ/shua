#%%
'''
39. Combination Sum
Medium


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
Example 4:

Input: candidates = [1], target = 1
Output: [[1]]
Example 5:

Input: candidates = [1], target = 2
Output: [[1,1]]
 

Constraints:

1 <= candidates.length <= 30
1 <= candidates[i] <= 200
All elements of candidates are distinct.
1 <= target <= 500
'''
import collections
class Solution:
    def combinationSum_uselist(self, candidates, target: int) -> [[int]]:
        
        ## space = O(target**2)
        ## time = O(len(candidtes)*target)
        
        candidates =list(set( [tt for tt in candidates if tt<=target ]))
        dp = [ [] for _ in range(target+1)]
        dp[0] = [ [0] ]
        for c in candidates:

            for w in range(c,target+1):
                if len(dp[w-c]) >0:
                    dp_tmp = [[x for x in ll] for ll in dp[w-c]]
                    for v in dp_tmp:
                        v.append(c)
                    dp[w] += dp_tmp
        res = [tt[1:] for tt in dp[target]]
        return res
                    
    ## try use string
    def combinationSum_string(self, candidates, target: int) -> [[int]]:
        
        ## space = O(target**2)
        ## time = O(len(candidtes)*target)
        candidates =list(set( [tt for tt in candidates if tt<=target ]))
        candidates.sort()
        dp = [ [''] for _ in range(target+1)]
        dp[0] = [ '0' ]
        for c in candidates:
            for w in range(c,target+1):
                if len(dp[w-c]) >0:
                    # dp_tmp = [[x for x in ll] for ll in dp[w-c]]
                    for v in dp[w-c]:
                        if v!='':
                            dp[w] += ['_'.join( [v,str(c)]) ]
                        
        res = [tt.split('_')[1:] for tt in dp[target]]
        res = [ [int(s) for s in tt] for tt in res if len(tt)>0]
        print(dp[target])
        return res




# %%
candidates = [2,3,6,7]
target = 7

candidates = [2,3,5]
target = 8

solu = Solution()
solu.combinationSum_string(candidates, target)
# %%
