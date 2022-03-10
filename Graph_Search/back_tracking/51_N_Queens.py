'''
51. N-Queens

The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space, respectively.

a queen can move vertial, horizontal, diagonal, antidiagonal as far as possible till it hits something
 

Example 1:


Input: n = 4
Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above
Example 2:

Input: n = 1
Output: [["Q"]]
 

Constraints:

1 <= n <= 9
'''


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:## each previous row will provide nonavailable moves
        ## DFS: backtracking
        ## each row only one choice
        ## available_moves[i][j] if values (i,j) are available
        res = []
        def dfs(rowi,available_moves,traces):
            
            if rowi == n:
                res.append([_ for _ in traces])
                return
            
            if sum(available_moves[rowi] )== 0:
                return ## no available movies
                
                        
            
            for coli in range(n):
                if available_moves[rowi][coli] == 0:
                    continue
                    
                cur_available_moves = [ [_ for _ in rm] for rm in available_moves]
                ## update moves, we only need to care about next rows, no need to update previous rows
                # all column elts become unavailable
                for ir in range(n):
                    cur_available_moves[ir][coli] = 0
                    
                ## diagnal
                d = 1
                while rowi+d<n and coli+d<n:
                    cur_available_moves[rowi+d][coli+d] = 0
                    d += 1
                d = 1
                while rowi+d<n and coli-d>=0:
                    cur_available_moves[rowi+d][coli-d] = 0
                    d += 1
                traces.append(coli)
                
                dfs(rowi+1, cur_available_moves, traces)
                
                traces.pop()
        
        def translate_moves(r):
            move = [["." for _ in range(n)] for _ in range(n)]
            for i,k in enumerate(r):
                move[i][k] = "Q"
                
            move = ["".join(r) for r in move]
            return move
        
        available_moves = [ [1 for _ in range(n)] for _ in range(n)]
        dfs(0,available_moves,[])
        
        
        res = [translate_moves(r) for r in res]
        return res
