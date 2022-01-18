'''
37. Sudoku Solver
Hard

4362

137

Add to List

Share
Write a program to solve a Sudoku puzzle by filling the empty cells.

A sudoku solution must satisfy all of the following rules:

Each of the digits 1-9 must occur exactly once in each row.
Each of the digits 1-9 must occur exactly once in each column.
Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
The '.' character indicates empty cells.

 

Example 1:


Input: board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
Output: [["5","3","4","6","7","8","9","1","2"],["6","7","2","1","9","5","3","4","8"],["1","9","8","3","4","2","5","6","7"],["8","5","9","7","6","1","4","2","3"],["4","2","6","8","5","3","7","9","1"],["7","1","3","9","2","4","8","5","6"],["9","6","1","5","3","7","2","8","4"],["2","8","7","4","1","9","6","3","5"],["3","4","5","2","8","6","1","7","9"]]
Explanation: The input board is shown above and the only valid solution is shown below:


 

Constraints:

board.length == 9
board[i].length == 9
board[i][j] is a digit or '.'.
It is guaranteed that the input board has only one solution.
'''

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        ## get 3X3 nbd of i,j
        def get_nbd(i,j):
            ## upper left corner
            i0,j0 = 3*(i//3),3*(j//3)
            
            for di in range(3):
                for dj in range(3):
                    yield (i0 + di, j0 + dj)
                    
        ## find valid digits if any
        def testValid(x,y):
            digits = [0]*(10)

            ## row_existing
            for i in range(9):
                if board[x][i] == ".":
                    continue
                digits[int(board[x][i])] = 1

            ## col_existing
            for i in range(9):
                if board[i][y] == ".":
                    continue
                digits[int(board[i][y])] = 1

            if sum(digits) == 9:
                return []
            
            ## neighborhood 
            for i,j in get_nbd(x,y):
                if board[i][j] == ".":
                    continue
                digits[int(board[i][j])] = 1

            return [str(k) for k in range(1,10) if digits[k]==0]

            
            
            
        def dfs(x,y,board):
            if y>=9:
                return dfs(x+1,0,board)
                
            elif x>=9: ## termination
                return True

            elif board[x][y]!='.':
                return dfs(x,y+1,board)  
            else:
                digits = testValid(x,y)
                for i in digits:
                    board[x][y] = i
                    flag = dfs(x,y+1,board)
                    if flag:
                        return True
                    board[x][y] = "."

        
        dfs(0,0,board)
        
        
                    