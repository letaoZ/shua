'''
417. Pacific Atlantic Water Flow
Medium

2923

688

Add to List

Share
There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean. The Pacific Ocean touches the island's left and top edges, and the Atlantic Ocean touches the island's right and bottom edges.

The island is partitioned into a grid of square cells. You are given an m x n integer matrix heights where heights[r][c] represents the height above sea level of the cell at coordinate (r, c).

The island receives a lot of rain, and the rain water can flow to neighboring cells directly north, south, east, and west if the neighboring cell's height is less than or equal to the current cell's height. Water can flow from any cell adjacent to an ocean into the ocean.

Return a 2D list of grid coordinates result where result[i] = [ri, ci] denotes that rain water can flow from cell (ri, ci) to both the Pacific and Atlantic oceans.

 

Example 1:


Input: heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
Example 2:

Input: heights = [[2,1],[1,2]]
Output: [[0,0],[0,1],[1,0],[1,1]]
 

Constraints:

m == heights.length
n == heights[r].length
1 <= m, n <= 200
0 <= heights[r][c] <= 105
'''

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        ## for each cell (x,y); res[(x,y)] = 0,1,2,3; 0--no ocean, 1 pacific, 2 atlantic 3--all
        
        res = dict() ## cell to num
        results = [] ## whenever a cell reaches both (value=3), add it to results        
        m,n = len(heights), len(heights[0])
        atlantic = collections.deque()
        pacific = collections.deque()
        for i in range(m):
            atlantic.append((i,n-1))
            pacific.append((i,0))
        
        for i in range(n):
            pacific.append( (0,i))
            atlantic.append( (m-1,i))
        
        ## work on both
        def bfs(pacific,m,n):
            res_pacific = set()
            visited = [[0]*n for _ in range(m)]
            while pacific:
                x, y = pacific.popleft()
                res_pacific.add((x,y))
                visited[x][y] = 1
                for dx, dy in [(0,1),(0,-1),(1,0),(-1,0)]:
                    xi, yi = x+dx, y+dy
                    if xi>=m or xi<0 or yi>=n or yi<0 or visited[xi][yi]:
                        continue
                    if heights[xi][yi]<heights[x][y]:
                        continue
                    visited[xi][yi] = 1

                    pacific.append((xi,yi))

            return res_pacific
                
        res_pacific = bfs(pacific,m,n)
        # print(res_pacific)
        res_atlantic = bfs(atlantic,m,n)
        # print(res_atlantic)
        res = list(res_pacific.intersection(res_atlantic))
        res.sort()
        res = [[a,b] for a,b in res]
        return res