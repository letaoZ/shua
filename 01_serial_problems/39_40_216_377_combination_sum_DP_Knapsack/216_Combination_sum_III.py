'''
216. Combination Sum III
Medium

Find all valid combinations of k numbers that sum up to n such that the following conditions are true:

Only numbers 1 through 9 are used.
Each number is used at most once.
Return a list of all possible valid combinations. The list must not contain the same combination twice, and the combinations may be returned in any order.

 

Example 1:

Input: k = 3, n = 7
Output: [[1,2,4]]
Explanation:
1 + 2 + 4 = 7
There are no other valid combinations.
Example 2:

Input: k = 3, n = 9
Output: [[1,2,6],[1,3,5],[2,3,4]]
Explanation:
1 + 2 + 6 = 9
1 + 3 + 5 = 9
2 + 3 + 4 = 9
There are no other valid combinations.
Example 3:

Input: k = 4, n = 1
Output: []
Explanation: There are no valid combinations. [1,2,1] is not valid because 1 is used twice.
Example 4:

Input: k = 3, n = 2
Output: []
Explanation: There are no valid combinations.
Example 5:

Input: k = 9, n = 45
Output: [[1,2,3,4,5,6,7,8,9]]
Explanation:
1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 = 45
​​​​​​​There are no other valid combinations.
 

Constraints:

2 <= k <= 9
1 <= n <= 60


'''


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        if 45 < n:
            return []
        if n==45:
            return [list(range(1,10))] if k==9 else []
        dp = [ [] for _ in range(n+1)]
        dp[0] = ['0']
        for c in range(1,9+1):
            for w in reversed(range(c, n+1)):
                
                if len(dp[w-c]) > 0:
                    for ll in dp[w-c]:
                        
                        ll = ll.split('_') + [str(c)]
                        if len(ll)>k+1: 
                            continue
                        ll = '_'.join(ll)
                        if ll not in dp[w]:
                            dp[w].append(ll)
                            
                            
        
        res = [tt.split('_')[1:] for tt in dp[n] if len(tt)>=1]
        res = [[int(ss) for ss in tt] for tt in res if len(tt) == k]
        return res

    def combinationSum3_dfs_backtracking(self, k, n):
        
        if 45 < n:
            return []
        if n==45:
            return [list(range(1,10))] if k==9 else []
        
        def dfs( nums, k, n, path, ret):
            if k < 0 or n < 0:
                return 
            if k == 0 and n == 0:
                ret.append(path)
            for i in ( range(len(nums)) ):
                dfs(nums[i+1:], k-1, n-nums[i], path+[nums[i]], ret)
        ret = []
        dfs(list(range(1, 10)), k, n, [], ret)
        return ret

    def combinationSum3_dfs_tiny_space_saving(self, k, n):
        
        if 45 < n:
            return []
        if n==45:
            return [list(range(1,10))] if k==9 else []
        
        def dfs( mn_n, k, n, path, ret):
            if k < 0 or n < 0 :
                return 
            if k == 0 and n == 0:
                ret.append(path)
            for i in range(mn_n+1,9+1):
                dfs(i, k-1, n-i, path+[i], ret)
        ret = []
        dfs(0, k, n, [], ret)
        return ret
