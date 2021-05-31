class Solution:
    ## requirement:         Do not return anything, modify board in-place instead.

    def solve(self, board:list[list[str]]) -> None:

        ## only none transferable ones are the ones on the boundary
        ## and connected to the boundary

        M, N = len(board), len(board[0])


        def searching(board,i,j,marker):

            if i >=M or j>= N or i<0 or j<0:
                return
            if board[i][j] == 'X' or board[i][j] == marker:
                return 
            board[i][j] = marker
            for dx, dy in [(0,1),(-1,0),(1,0),(0,-1)]:
                x,y = i+dx, j+dy

                searching(board,x,y,marker)

            return 
        
        for i in range(M):
            if board[i][0] == 'O':
                searching(board,i,0,'N')## cannot connect
            if board[i][N-1] == 'O':
                searching(board,i,N-1,'N')## cannot connect

        for i in range(N):
            if board[0][i] == 'O':
                searching(board,0,i,'N')## cannot connect
            if board[M-1][i] == 'O':
                searching(board,M-1,i,'N')## cannot connect

        ## the rest can connect
        for i in range(M):
            for j in range(N):
                if board[i][j] == 'N':
                    board[i][j] = 'O'

                elif board[i][j] == 'O':
                    board[i][j] = 'X'

solu = Solution()        
board = [["X","O","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
board = [["O"]]
solu.solve(board)

print(board)