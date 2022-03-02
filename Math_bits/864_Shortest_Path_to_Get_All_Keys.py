'''
864. Shortest Path to Get All Keys
Hard

734

25

Add to List

Share
You are given an m x n grid grid where:

'.' is an empty cell.
'#' is a wall.
'@' is the starting point.
Lowercase letters represent keys.
Uppercase letters represent locks.
You start at the starting point and one move consists of walking one space in one of the four cardinal directions. You cannot walk outside the grid, or walk into a wall.

If you walk over a key, you can pick it up and you cannot walk over a lock unless you have its corresponding key.

For some 1 <= k <= 6, there is exactly one lowercase and one uppercase letter of the first k letters of the English alphabet in the grid. This means that there is exactly one key for each lock, and one lock for each key; and also that the letters used to represent the keys and locks were chosen in the same order as the English alphabet.

Return the lowest number of moves to acquire all keys. If it is impossible, return -1.

 

Example 1:


Input: grid = ["@.a.#","###.#","b.A.B"]
Output: 8
Explanation: Note that the goal is to obtain all the keys not to open all the locks.
Example 2:


Input: grid = ["@..aA","..B#.","....b"]
Output: 6
Example 3:


Input: grid = ["@Aa"]
Output: -1
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 30
grid[i][j] is either an English letter, '.', '#', or '@'.
The number of keys in the grid is in the range [1, 6].
Each key in the grid is unique.
Each key in the grid has a matching lock.
'''

class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        m, n = len(grid), len(grid[0])
# \        return
        ## find start and number of keys
        j = n
        nkeys = 0
        queue = collections.deque()
        # grid = [list(r) for r in grid]
        origin = (0,0)
        for i,r in enumerate(grid):
            for j,c in enumerate(r):
                if c == '@':
                    queue.append((i,j, 0))
                    origin = (i,j)
                if 0<=ord(c) - ord('a')<26:
                    nkeys += 1
        if nkeys == 0:
            return 0
        
        dirs = [(0,1),(0,-1),(-1,0),(1,0)]
        visited = [ [ [0 for _ in range(1<<nkeys)] for _ in range(n)] for _ in range(m)]
        visited[origin[0]][origin[1]][0] = 1
        level = 0
        print(nkeys)
        keys = 0
        while queue:
            L = len(queue)
            for _ in range(L):
                a, b, cur_keys = queue.popleft()  
                # print(cur_keys)
                if (cur_keys == (1<<nkeys) - 1): return level
                for dx, dy in dirs:
                    keys = cur_keys
                    x, y = a + dx, b + dy
                    if not (0<=x <m  and 0<=y<n):
                        continue
                    if '#' == grid[x][y]:
                        continue
                    if "a"<=grid[x][y]<="z": ## found a key
                        # print(grid[x][y])
                        keys = (cur_keys | (1<<(ord(grid[x][y] ) - ord('a'))) )
                        # print(f"grid[x][y] {grid[x][y]} cur_keys {cur_keys} keys {keys}")

                        if keys == ((1<<nkeys) - 1):
                            return level + 1
                        
                    elif "A"<= grid[x][y]<="Z": ## lock
                        ## see if we have a key
                        # print(f"cur_keys {cur_keys}, {(ord(grid[x][y] ) - ord('A'))}")
                        # print((cur_keys & (1<<(ord(grid[x][y] ) - ord('A'))) ))
                        if (cur_keys & (1<<(ord(grid[x][y] ) - ord('A'))) ) == 0:
                            continue
            
                    if visited[x][y][keys]:
                        continue
                    
                    visited[x][y][keys] = 1
                    queue.append((x,y, keys))
            level += 1

        # print(keys,level)
        return -1
                    
                    
            