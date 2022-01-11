'''1368. Minimum Cost to Make at Least One Valid Path in a Grid
Hard

879

7

Add to List

Share
Given an m x n grid. Each cell of the grid has a sign pointing to the next cell you should visit if you are currently in this cell. The sign of grid[i][j] can be:

1 which means go to the cell to the right. (i.e go from grid[i][j] to grid[i][j + 1])
2 which means go to the cell to the left. (i.e go from grid[i][j] to grid[i][j - 1])
3 which means go to the lower cell. (i.e go from grid[i][j] to grid[i + 1][j])
4 which means go to the upper cell. (i.e go from grid[i][j] to grid[i - 1][j])
Notice that there could be some signs on the cells of the grid that point outside the grid.

You will initially start at the upper left cell (0, 0). A valid path in the grid is a path that starts from the upper left cell (0, 0) and ends at the bottom-right cell (m - 1, n - 1) following the signs on the grid. The valid path does not have to be the shortest.

You can modify the sign on a cell with cost = 1. You can modify the sign on a cell one time only.

Return the minimum cost to make the grid have at least one valid path.

 

Example 1:


Input: grid = [[1,1,1,1],[2,2,2,2],[1,1,1,1],[2,2,2,2]]
Output: 3
Explanation: You will start at point (0, 0).
The path to (3, 3) is as follows. (0, 0) --> (0, 1) --> (0, 2) --> (0, 3) change the arrow to down with cost = 1 --> (1, 3) --> (1, 2) --> (1, 1) --> (1, 0) change the arrow to down with cost = 1 --> (2, 0) --> (2, 1) --> (2, 2) --> (2, 3) change the arrow to down with cost = 1 --> (3, 3)
The total cost = 3.
Example 2:


Input: grid = [[1,1,3],[3,2,2],[1,1,4]]
Output: 0
Explanation: You can follow the path from (0, 0) to (2, 2).
Example 3:


Input: grid = [[1,2],[4,3]]
Output: 1

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 100
1 <= grid[i][j] <= 4
'''

class Solution:

    def minCost(self, grid: List[List[int]]) -> int:
        ## bfs + dfs
        ## O(MN)
        directions = [(), (0,1) ,(0,-1) , (1,0), (-1,0)]
        m, n= len(grid), len(grid[0])

            
        ## for each node; dfs its all reachable, update cost
        ## then bfs all other directions of all nodes in the reachable --> with extra cost
        ## keep track if the node is pointing out
        
        
        ## dp[x][y] num of changes needed to reach x,y
        dp =[ [float('inf')]*n for _ in range(m)]
        
        def dfs(x,y,cur_change,queue):
            if not (0<=x<m and 0<=y<n and dp[x][y]==float('inf')):
                return
            queue.append((x,y))
            dp[x][y] = cur_change
            dx, dy = directions[grid[x][y]]    
            dfs(x+dx, y+dy, cur_change,queue)
            
        queue = collections.deque()
        queue.append((0,0))
        
        nchanges = 0
        while queue:
            
            L = len(queue)
            for i in range(L): ## note: here we don't pop anything yet. we want to find all nodes with same nchanges reachable.
                x,y = queue[i]
                dp[x][y] = nchanges
                dx, dy = directions[grid[x][y]] 
                dfs(x+dx,y+dy, nchanges,queue,)
                if dp[-1][-1] != float('inf'):
                    return nchanges
                
            ## Now we start make changes and add notes for next "bfs"
            nchanges += 1
            for _ in range( len(queue)):
                x,y = queue.popleft()
                for i in range(1,5):
                    if grid[x][y] == i:
                        continue
                    xi, yi = x + directions[i][0], y+directions[i][1]
                    if (0<=xi<m and 0<=yi<n and dp[xi][yi]==float('inf')):
                        if xi==m-1 and yi==n-1:
                            return nchanges
                        queue.append((xi,yi))
                    
        # for r in dp:
        #     print(r)
        return dp[-1][-1]

            

