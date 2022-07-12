'''
79. Word Search
Medium
Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

 

Example 1:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true
Example 2:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true
Example 3:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Output: false
 

Constraints:

m == board.length
n = board[i].length
1 <= m, n <= 6
1 <= word.length <= 15
board and word consists of only lowercase and uppercase English letters.
 

Follow up: Could you use search pruning to make your solution faster with a larger board?
'''

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        ## DFS: time O(m*n)
        
        def dfs(iw,i,j,visited, m, n, res):
            # print("dfs: ")
            
            '''
            iw := visited iw index of word
            i, j := i, j th entry of the board
            visited := positions visited on the board
            m, n := len(board), len(board[0])
            res := True if found the word
            '''
            if iw == len(word):
                res[0] = True
                return 

            # print(iw, word[iw])
            for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                
                x, y = i + dx, j + dy
                if not ( 0<= x < m and 0<= y < n):
                    continue
                # print(i,j,board[x][y])
                if visited[x][y]:
                    continue
                if not word[iw] == board[x][y]:
                    continue

                visited[x][y] = 1
                dfs(iw + 1, x, y, visited, m, n, res)
                visited[x][y] = 0

            return False
        
        m, n = len(board), len(board[0])
        visited = [[0]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if word[0] != board[i][j]:
                    continue
                visited = [[0]*n for _ in range(m)]
                res = [False]
                # print('start: ',i,j,board[i][j])
                visited[i][j] = 1
                dfs(1,i,j,visited,m,n, res)
                if res[0]:
                    return True
                                    
                
        return False