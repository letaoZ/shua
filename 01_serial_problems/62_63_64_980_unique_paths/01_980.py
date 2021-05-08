'''
980. Unique Paths III
Hard

On a 2-dimensional grid, there are 4 types of squares:

1 represents the starting square.  There is exactly one starting square.
2 represents the ending square.  There is exactly one ending square.
0 represents empty squares we can walk over.
-1 represents obstacles that we cannot walk over.
Return the number of 4-directional walks from the starting square to the ending square, that walk over every non-obstacle square exactly once.

 

Example 1:

Input: [[1,0,0,0],[0,0,0,0],[0,0,2,-1]]
Output: 2
Explanation: We have the following two paths: 
1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2)
2. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2)
Example 2:

Input: [[1,0,0,0],[0,0,0,0],[0,0,0,2]]
Output: 4
Explanation: We have the following four paths: 
1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2),(2,3)
2. (0,0),(0,1),(1,1),(1,0),(2,0),(2,1),(2,2),(1,2),(0,2),(0,3),(1,3),(2,3)
3. (0,0),(1,0),(2,0),(2,1),(2,2),(1,2),(1,1),(0,1),(0,2),(0,3),(1,3),(2,3)
4. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2),(2,3)
Example 3:

Input: [[0,1],[2,0]]
Output: 0
Explanation: 
There is no path that walks over every empty square exactly once.
Note that the starting and ending square can be anywhere in the grid.
 

Note:

1 <= grid.length * grid[0].length <= 20

'''



class Solution:
    def uniquePathsIII_extra_space(self, grid: List[List[int]]) -> int:
        m = len(grid)
        if m == 0: 
            return 0
        
        n = len(grid[0])
        if n == 0:
            return 0
        
        
        visited = [ [0]*n for _ in range(m) ]
        
        ## find begin and end
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    S0,S1 = i,j
                if grid[i][j] == 2:
                    E0,E1 = i,j


        ## keep track of number of paths
        cnt = [0]
        

        ## check if all nodes are visited
        def check_visit(m,n,grid,visited):
            for i in range(m):
                for j in range(n):
                    if grid[i][j] != -1 and visited[i][j] != 1:
                        return False
            return True
                    
        ## M = mn, time = O(3**M), space = O(M)
        def searching(i,j,m,n,grid,visited,cnt):
            if i>=m or i<0:
                return
            if j>=n or j<0:
                return
            if visited[i][j] == 1:
                return
            if grid[i][j]==-1:
                return

            visited[i][j] = 1
            
            searching(i+1,j,m,n,grid,visited,cnt)
            searching(i,j+1,m,n,grid,visited,cnt) 
            searching(i-1,j,m,n,grid,visited,cnt) 
            searching(i,j-1,m,n,grid,visited,cnt)
            if i == E0 and j==E1:
                if check_visit(m,n,grid,visited):
                    cnt[0] += 1
            
            visited[i][j] = 0
        searching(S0,S1,m,n,grid,visited,cnt)

        return cnt[0]


    def uniquePathsIII_space_saving(self, grid: List[List[int]]) -> int:
        m = len(grid)
        if m == 0: 
            return 0
        
        n = len(grid[0])
        if n == 0:
            return 0
        
        
        remain = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == -1:
                    continue
                if grid[i][j] == 1:
                    S0,S1 = i,j
                if grid[i][j] == 2:
                    E0,E1 = i,j

                remain += 1

        cnt = [0]

        ## update grid to replace visited                    
        def searching(i,j,m,n,grid,cnt,remain):
            if i>=m or i<0:
                return
            if j>=n or j<0:
                return
            if grid[i][j] == 8:
                return
            if grid[i][j]==-1:
                return

            tmp = grid[i][j]
            grid[i][j] = 8
            remain -= 1
            searching(i+1,j,m,n,grid,cnt,remain)
            searching(i,j+1,m,n,grid,cnt,remain) 
            searching(i-1,j,m,n,grid,cnt,remain) 
            searching(i,j-1,m,n,grid,cnt,remain)
            if i == E0 and j==E1:
                if remain <= 0:
                    cnt[0] += 1
            grid[i][j] = tmp
            
        searching(S0,S1,m,n,grid,cnt,remain)

        return cnt[0]
    
    
    