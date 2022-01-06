'''
286. Walls and Gates
Medium

2060

34

Add to List

Share
You are given an m x n grid rooms initialized with these three possible values.

-1 A wall or an obstacle.
0 A gate.
INF Infinity means an empty room. We use the value 231 - 1 = 2147483647 to represent INF as you may assume that the distance to a gate is less than 2147483647.
Fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate, it should be filled with INF.

 

Example 1:


Input: rooms = [[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]]
Output: [[3,-1,0,1],[2,2,1,-1],[1,-1,2,-1],[0,-1,3,4]]
Example 2:

Input: rooms = [[-1]]
Output: [[-1]]
 

Constraints:

m == rooms.length
n == rooms[i].length
1 <= m, n <= 250
rooms[i][j] is -1, 0, or 231 - 1.
'''

class Solution:
    def wallsAndGates_DFS(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        INF = 2147483647
        
        ## find where the gates are

        
        ## dfs
        M,N = len(rooms), len(rooms[0])
        def dfs(rooms,x,y):
            
            if x>=M or y>=N or x<0 or y<0 or rooms[x][y] == -1:
                return INF
            
            for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
                xi, yi = x+dx, y+dy ## where the next  steps are
                if xi>=M or yi>=N or xi<0 or yi<0 or rooms[xi][yi] == -1:
                    continue
                
                if rooms[xi][yi]>rooms[x][y]+1:
                    rooms[xi][yi] = rooms[x][y]+1
                    dfs(rooms,xi,yi)
        
        for x in range(M):
            for y in range(N):
                if rooms[x][y] == 0:
                    dfs(rooms, x, y)
                    
                    
    def wallsAndGates_BFS(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        INF = 2147483647
        M,N = len(rooms), len(rooms[0])

        queue = collections.deque()
        ## find where the gates are
        for i in range(M):
            for j in range(N):
                if rooms[i][j] == 0:
                    queue.append((i,j))
        cnt = 0
        while queue:
            x,y = queue.popleft()
            ## the first few popleft are all from dist 1 points from a gate
            for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
                xi, yi = x+dx, y+dy ## where the next  steps are
                if xi>=M or yi>=N or xi<0 or yi<0 or rooms[xi][yi] == -1:
                    continue
                if rooms[xi][yi] == INF:
                    rooms[xi][yi] = 1 + rooms[x][y]
                    queue.append((xi,yi))
                    
                    