'''
36. Valid Sudoku
Medium

5719

764

Add to List

Share
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.
 

Example 1:


Input: board = 
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: true
Example 2:

Input: board = 
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: false
Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.
 

Constraints:

board.length == 9
board[i].length == 9
board[i][j] is a digit 1-9 or '.'.

'''
from typing import *

class Solution:
    def checkSub(self,board,i,j):
        '''
        i, j := upper left corner of the 3x3 subboard
        '''
        visited = set()
        for x in range(i, i+3):
            for y in range(j, j+3):
                if board[x][y] == '.': continue
                if board[x][y] in visited: return False
                visited.add(board[x][y])
        return True
        
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        ## row check
        for r in board:
            r_n = [x for x in r if x != "."]
            if len(r_n) != len(set(r_n)):
                return False
            
        
        
        ## column check
        for j in range(9):
            visited = set()
            for i in range(9):
                if board[i][j] in visited: return False
                if board[i][j] == ".": continue
                visited.add(board[i][j])
            
        ## 3x3 check
        for i in range(0, 9, 3):
            for j in range(0, 9 ,3):
                if not self.checkSub(board, i, j):
                    return False
                
        return True