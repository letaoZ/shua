'''
265. Paint House II
Hard

874

31

Add to List

Share
There are a row of n houses, each house can be painted with one of the k colors. The cost of painting each house with a certain color is different. You have to paint all the houses such that no two adjacent houses have the same color.

The cost of painting each house with a certain color is represented by an n x k cost matrix costs.

For example, costs[0][0] is the cost of painting house 0 with color 0; costs[1][2] is the cost of painting house 1 with color 2, and so on...
Return the minimum cost to paint all houses.

 

Example 1:

Input: costs = [[1,5,3],[2,9,4]]
Output: 5
Explanation:
Paint house 0 into color 0, paint house 1 into color 2. Minimum cost: 1 + 4 = 5; 
Or paint house 0 into color 2, paint house 1 into color 0. Minimum cost: 3 + 2 = 5.
Example 2:

Input: costs = [[1,3],[2,4]]
Output: 5

Constraints:

costs.length == n
costs[i].length == k
1 <= n <= 100
2 <= k <= 20
1 <= costs[i][j] <= 20
'''

class Solution:
    def minCostII_mem_N(self, costs: List[List[int]]) -> int:

        
        ## dp[k][i] := min cost for painting house[...k] if paint house[k] with color i
        ## dp[k][i] = min(dp[k-1][j] + costs[k][j]) where j!=i 
        nhouses = len(costs)
        ncolors = len(costs[0])
        dp = [[float('inf')]*ncolors for _ in range(nhouses)]
        
        for i in range(ncolors):
            dp[0][i] = costs[0][i]
            
        for k in range(1,nhouses):
            for c in range(ncolors):
                for j in range(ncolors):
                    if j==c:
                        continue
                    dp[k][c] = min(dp[k][c], dp[k-1][j] + costs[k][c])
                    
                    
        res = min(dp[nhouses-1])
        
        return res

    def minCostII(self, costs: List[List[int]]) -> int:

        
        ## dp[k][i] := min cost for painting house[...k] if paint house[k] with color i
        ## dp[k][i] = min(dp[k-1][j] + costs[k][j]) where j!=i 
        nhouses = len(costs)
        ncolors = len(costs[0])
        dp = [float('inf')]*ncolors 
        
        for i in range(ncolors):
            dp[i] = costs[0][i]
            
        for k in range(1,nhouses):
            dp_tmp = [float("inf")]*ncolors
            for c in range(ncolors):
                for j in range(ncolors):
                    if j==c:
                        continue
                        
                    dp_tmp[c] = min(dp_tmp[c], dp[j] + costs[k][c])
                    
            dp = [_ for _ in dp_tmp]
        res = min(dp)
        
        return res
                    