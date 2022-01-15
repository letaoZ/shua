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
    def solveNQueens(self, n: int) -> List[List[str]]:
        ## DFS: backtracking
        ## each row only one choice
        ## indicate if values are used
        valid = [[1]*n for _ in range(n)]
        res = []
        
        ## r=row number
        ## trace := column number we used
        def dfs(r,trace,valid,res):
            if r >= n: ## 
                if len(trace) == n:
                    res.append([t for t in trace])
                return
            if sum(valid[r]) == 0: ## no valid, means we cannot get a path 
                return
            
            for c in range(n):
                if not valid[r][c]:
                    continue
                
                ## for backtracking
                tmp_valid = [ [v for v in row] for row in valid]
                
                ## assign invalid move
                for j in range(n):
                    tmp_valid[j][c] = 0
                    tmp_valid[r][j] = 0
                    
                        
                    if r+j<n and c-j>=0:
                        tmp_valid[r+j][c-j] = 0
                        
                    if r+j<n and c+j<n:
                        tmp_valid[r+j][c+j] = 0
                        
                    ## since row-wise we only go forward, we don't need to change backward row values
                    if r-j>=0 and c-j>=0:
                        tmp_valid[r-j][c-j] = 0
                        
                    if r-j>=0 and c+j<n:
                        tmp_valid[r-j][c+j] = 0

                trace.append(c)
                dfs(r+1,trace,tmp_valid,res)
                trace.pop()
                
        def translate_path(n,k):
            d = ["."]*n
            d[k] = 'Q'
            return ''.join(d)
        
        
        dfs(0,[],valid,res)
        
        for i,r in enumerate(res):
            mat = ['']*n
            for j in range(n):
                mat[j] = translate_path(n,r[j])
                
            res[i] = mat
            
        return res
                
        