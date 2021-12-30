'''
256. Paint House
Medium

1621

109

Add to List

Share
There is a row of n houses, where each house can be painted one of three colors: red, blue, or green. The cost of painting each house with a certain color is different. You have to paint all the houses such that no two adjacent houses have the same color.

The cost of painting each house with a certain color is represented by an n x 3 cost matrix costs.

For example, costs[0][0] is the cost of painting house 0 with the color red; costs[1][2] is the cost of painting house 1 with color green, and so on...
Return the minimum cost to paint all houses.

 

Example 1:

Input: costs = [[17,2,17],[16,16,5],[14,3,19]]
Output: 10
Explanation: Paint house 0 into blue, paint house 1 into green, paint house 2 into blue.
Minimum cost: 2 + 5 + 3 = 10.
Example 2:

Input: costs = [[7,6,2]]
Output: 2
 

Constraints:

costs.length == n
costs[i].length == 3
1 <= n <= 100
1 <= costs[i][j] <= 20
'''
class Solution:
    def minCost_mem_N(self, costs: List[List[int]]) -> int:
        
        ## dp[k][i] := min cost for painting house[...k] if paint house[k] with color i
        ## dp[k][i] = min(dp[k-1][j] + costs[k][j]) where j!=i 
        nhouses = len(costs)
        dp = [[float('inf')]*3 for _ in range(nhouses)]
        
        for i in range(3):
            dp[0][i] = costs[0][i]
            
        for k in range(1,nhouses):
            for c in range(3):
                for j in range(3):
                    if j==c:
                        continue
                    dp[k][c] = min(dp[k][c], dp[k-1][j] + costs[k][c])
                    
                    
        res = min(dp[nhouses-1])
        
        return res
                    
    def minCost_mem_reduce(self, costs: List[List[int]]) -> int:
        
        ## dp[k][i] := min cost for painting house[...k] if paint house[k] with color i
        ## dp[k][i] = min(dp[k-1][j] + costs[k][j]) where j!=i 
        ## do mem reduction
        nhouses = len(costs)
        dp = [float('inf')]*3
        
        for i in range(3):
            dp[i] = costs[0][i]
            
        for k in range(1,nhouses):
            dp_tmp = [float('inf')]*3
            for c in range(3):
                for j in range(3):
                    if j==c:
                        continue
                    
                    dp_tmp[c] = min(dp_tmp[c], dp[j] + costs[k][c])
            dp = [_ for _ in dp_tmp]
                    
        res = min(dp)
        
        return res
                    