'''286. Walls and Gates
Medium

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
Example 3:

Input: rooms = [[2147483647]]
Output: [[2147483647]]
Example 4:

Input: rooms = [[0]]
Output: [[0]]
 

Constraints:

m == rooms.length
n == rooms[i].length
1 <= m, n <= 250
rooms[i][j] is -1, 0, or 231 - 1.


'''


class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        M, N = len(rooms), len(rooms[0])
        INF = 2147483647
        def searching(rooms,prev, i, j):
            if i>=M or j>=N or i<0 or j<0:
                return 

            if rooms[i][j] == -1:
                return 
            
            if rooms[i][j] == 0 and prev!=-2:
                return
            
            if rooms[i][j] <= prev+1:
                return 
            rooms[i][j] =  prev+1 if rooms[i][j]!= 0 else 0
            for dx, dy in [(0,1),(1,0),(0,-1),(-1,0)]:
                
                x, y = i+dx, j + dy
                searching(rooms, rooms[i][j],x,y)
                
            return
                                  
                            
                
                
        for i in range(M):
            for j in range(N):
                if rooms[i][j] == 0:
                    
                    searching(rooms,-2 ,i,j)                    
        return rooms