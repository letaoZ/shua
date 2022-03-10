'''
77. Combinations
Medium

3492

117

Add to List

Share
Given two integers n and k, return all possible combinations of k numbers out of the range [1, n].

You may return the answer in any order.

 

Example 1:

Input: n = 4, k = 2
Output:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
Example 2:

Input: n = 1, k = 1
Output: [[1]]
 

Constraints:

1 <= n <= 20
1 <= k <= n

'''
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        def dfs(i, trace, k, n, res):
            if k == 0:
                res.append([_ for _ in trace])
                return
            
            for j in range(i, n+1):
                dfs(j+1, trace + [j], k-1, n, res)
        
        dfs(1,[], k, n, res)
        return res
        
                