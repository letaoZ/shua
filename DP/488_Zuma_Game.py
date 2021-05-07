'''
488. Zuma Game
Hard

Think about Zuma Game. You have a row of balls on the table, colored red(R), yellow(Y), blue(B), green(G), and white(W). You also have several balls in your hand.

Each time, you may choose a ball in your hand, and insert it into the row (including the leftmost place and rightmost place). Then, if there is a group of 3 or more balls in the same color touching, remove these balls. Keep doing this until no more balls can be removed.

Find the minimal balls you have to insert to remove all the balls on the table. If you cannot remove all the balls, output -1.

 

Example 1:

Input: board = "WRRBBW", hand = "RB"
Output: -1
Explanation: WRRBBW -> WRR[R]BBW -> WBBW -> WBB[B]W -> WW
Example 2:

Input: board = "WWRRBBWW", hand = "WRBRW"
Output: 2
Explanation: WWRRBBWW -> WWRR[R]BBWW -> WWBBWW -> WWBB[B]WW -> WWWW -> empty
Example 3:

Input: board = "G", hand = "GGGGG"
Output: 2
Explanation: G -> G[G] -> GG[G] -> empty 
Example 4:

Input: board = "RBYYBBRRB", hand = "YRBGB"
Output: 3
Explanation: RBYYBBRRB -> RBYY[Y]BBRRB -> RBBBRRB -> RRRB -> B -> B[B] -> BB[B] -> empty 
 

Constraints:

You may assume that the initial row of balls on the table won’t have any 3 or more consecutive balls with the same color.
1 <= board.length <= 16
1 <= hand.length <= 5
Both input strings will be non-empty and only contain characters 'R','Y','B','G','W'.






## it seems like ONLY brutal force works
## consider the case: RRWWRRBBR and WB 
 RRWWRRB[W]BR will be the first step

'''

class Solution:
    def findMinStep(self, board: str, hand: str) -> int:

        def clean(board):
            stack = []
            for b in board:
                if stack and stack[-1][0] != b and stack[-1][1] >= 3:
                    stack.pop()
                if not stack or stack[-1][0] != b:
                    stack += [b, 1],
                else:
                    stack[-1][1] += 1
            if stack and stack[-1][1] >= 3:
                stack.pop()
            return ''.join([a*b for a,b in stack])

        @lru_cache(None)
        def dfs(board, hand):
            if not board:
                return 0
            if not hand:
                return float('inf')
            m = len(board)
            ans = float('inf')
            for j, b in enumerate(hand):
                new_hand = hand[:j] + hand[j+1:]
                for i in range(m + 1):
                    new_board = clean(board[:i] + b + board[i:])
                    ans = min(ans, 1 + dfs(new_board, new_hand))
            return ans
        
        ans = dfs(board, hand)
        return ans if ans < float('inf') else -1







class Solution1: ## slow and wrong... 
    def findMinStep_my_extremely_slowSolution(self, board: str, hand: str) -> int:
        ## Note the length is 16, so 
        ## 16 factorial we may still get an answer
        
        
        board = [ss for ss in board]
        handd = [ss for ss in hand]
        handd.sort()

        ## search just to insert one
        ## search to insert two
        
        def searching(board, hands):
            print('searching:',)
            sz = len(board)
            ## remove all 3 or more consecutives
            l = 0
            r = 0
            G = 0
            print('board before', board)

            while r<sz:
                G = 0
                k = r
                
                while k<sz:
                    if board[k] != board[r]:
                        break
                        
                    G += 1
                    k += 1

                if G<3:
                    for kk in range(G):
                        board[l] = board[r]
                        l += 1
                        r += 1    

            board = board[:l]
            sz = len(board)
            print('board after', board)

            if sz == 0:
                return 0
            if sz >= 3 and len(set(board) ) == 1:
                return 0            

            if sz == 1:
                if board[0] in hands and sum([1 for bb in hands if bb==board[0]])>=2:
                    
                    return 2
                else:
                    return float('inf')

            
            res_cur = float('inf')

            
            i = 0

            while i+1<sz:
                print(i, board,hands)
                if board[i] not in hands:
                    i += 1
                    continue
                    
                if board[i] != board[i+1]  and sum([1 for bb in hands if bb==board[i]])>=2:
                    handst = [ss for ss in hands]
                    handst.remove(board[i])
                    handst.remove(board[i])
                    restmp = 2 + searching(board[:i]+board[i+1:], handst)    
                    res_cur = min(res_cur, restmp)
                    i += 1
                    continue
                    
                if board[i] == board[i+1]:
                    if i+2<sz and  board[i]== board[i+2]:
                        restmp = searching(board[:i]+board[i+3:], hands)
                    else:
                        handst = [ss for ss in hands]
    
                        handst.remove(board[i])
                        print('board[:i]+board[i+2:]', board[:i]+board[i+2:])
                        restmp = 1+ searching(board[:i]+board[i+2:], handst)
                    res_cur = min(res_cur, restmp)
                    i += 2
                    continue
                i += 1
            return res_cur
        res = searching(board, handd)
        tmp = [1,2,3,4,4,3]
        tmp.remove(4)
        print(tmp)

        return res if res < float('inf') else -1
                                            
        
        
        
            
            
             
