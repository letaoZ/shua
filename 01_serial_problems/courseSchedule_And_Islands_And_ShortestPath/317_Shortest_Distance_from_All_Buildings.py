'''317. Shortest Distance from All Buildings
Hard

You are given an m x n grid grid of values 0, 1, or 2, where:

each 0 marks an empty land that you can pass by freely,
each 1 marks a building that you cannot pass through, and
each 2 marks an obstacle that you cannot pass through.
You want to build a house on an empty land that reaches all buildings in the shortest total travel distance. You can only move up, down, left, and right.

Return the shortest travel distance for such a house. If it is not possible to build such a house according to the above rules, return -1.

The total travel distance is the sum of the distances between the houses of the friends and the meeting point.

The distance is calculated using Manhattan Distance, where distance(p1, p2) = |p2.x - p1.x| + |p2.y - p1.y|.

 

Example 1:


Input: grid = [[1,0,2,0,1],[0,0,0,0,0],[0,0,1,0,0]]
Output: 7
Explanation: Given three buildings at (0,0), (0,4), (2,2), and an obstacle at (0,2).
The point (1,2) is an ideal empty land to build a house, as the total travel distance of 3+3+1=7 is minimal.
So return 7.
Example 2:

Input: grid = [[1,0]]
Output: 1
Example 3:

Input: grid = [[1]]
Output: -1
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 100
grid[i][j] is either 0, 1, or 2.
There will be at least one building in the grid.

'''


class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        ## find all buildings
        M, N = len(grid), len(grid[0])
        building = []
        for i in range(M):
            for j in range(N):
                if grid[i][j] == 1:
                    building.append((i,j))
                    
        ## keys of d are potential points to build home
        ## d[(x,y)][building] = distance from point(x,y) to each building
        d = collections.defaultdict(dict)

        for x,y in building:

            queue = collections.deque()
            queue.append((x,y))
            visited = [ [0]*N for _ in range(M)]
            dist = 1
            d[(x,y)][(x,y)] = 0
            while queue:
                a,b = queue.popleft()
                
                for dx,dy in [(0,1),(0,-1),(1,0),(-1,0)]:
                    a1,b1 = a+dx, b+dy
                  
                
                    if a1>=M or b1>=N or a1<0 or b1<0:
                        continue
                    if grid[a1][b1] in [1,2]: 
                        continue
                    if visited[a1][b1]:
                        continue
                    visited[a1][b1] = 1
                    d[(a1,b1)][(x,y)] = d[(a,b)][(x,y)] + 1
                    queue.append((a1,b1))
        nbuildings  = len(building)
        res = float('inf')
        for p,v in d.items():
            if p in building: continue
            # print(p)
            # print(v)
            if len(v)<nbuildings: continue
            ss = 0
            for _,dd in v.items():
                ss += dd

            res = min(res,ss)
        return res if res < float('inf') else -1