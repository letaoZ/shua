'''1406. Stone Game III
Hard


Alice and Bob continue their games with piles of stones. 
There are several stones arranged in a row, and each stone 
has an associated value which is an integer given in the 
array stoneValue.

Alice and Bob take turns, with Alice starting first. 
On each player's turn, that player can take 1, 2 or 3 stones 
from the first remaining stones in the row.

The score of each player is the sum of values of the stones taken. The score of each player is 0 initially.

The objective of the game is to end with the highest score, and the winner is the player with the highest score and there could be a tie. The game continues until all the stones have been taken.

Assume Alice and Bob play optimally.

Return "Alice" if Alice will win, "Bob" if Bob will win or "Tie" if they end the game with the same score.

 

Example 1:

Input: values = [1,2,3,7]
Output: "Bob"
Explanation: Alice will always lose. Her best move will be to take three piles and the score become 6. Now the score of Bob is 7 and Bob wins.
Example 2:

Input: values = [1,2,3,-9]
Output: "Alice"
Explanation: Alice must choose all the three piles at the first move to win and leave Bob with negative score.
If Alice chooses one pile her score will be 1 and the next move Bob's score becomes 5. The next move Alice will take the pile with value = -9 and lose.
If Alice chooses two piles her score will be 3 and the next move Bob's score becomes 3. The next move Alice will take the pile with value = -9 and also lose.
Remember that both play optimally so here Alice will choose the scenario that makes her win.
Example 3:

Input: values = [1,2,3,6]
Output: "Tie"
Explanation: Alice cannot win this game. She can end the game in a draw if she decided to choose all the first three piles, otherwise she will lose.
Example 4:

Input: values = [1,2,3,-1,-2,-3,7]
Output: "Alice"
Example 5:

Input: values = [-1,-2,-3]
Output: "Tie"

Constraints:

1 <= values.length <= 50000
-1000 <= values[i] <= 1000

pure computation without mem or dp: 3^sz time

'''






class Solution:
    def stoneGameIIIdp_1d_mem_topdown(self, stoneValue: List[int]) -> str:
        ## time reduction
        ## bottom up
        SZ = len(stoneValue)
        
        ## dp[i] max score Alice get starting from i 
        dp =[-float('inf')]*(SZ + 4
                            )
        
        ## added cushion
        for k in range(4):
            dp[SZ+k] = 0
            
        ## added cushion
        stoneValue = stoneValue + [0,0]
        
        for i in range(SZ-1,-1,-1):
            psum = 0
            for X in range(3):

                psum += stoneValue[i+X]
                
                dp[i] = max(
                    dp[i], psum - dp[i+X+1]
                           )
        diff = dp[0]

        if diff == 0:
            return 'Tie'
        elif diff > 0:
            return 'Alice'
        else:
            return 'Bob'
        
        
    def stoneGameIII_dp_2d_mem_topdown(self, stoneValue: List[int]) -> str:
        ## time = 3*SZ^2
        ##
        SZ = len(stoneValue)
        
        ## dp[X][i] max score you get starting from i by picking X many stones
        dp =[ [-float('inf')]*SZ for _ in range(4) ]
        
        def searching(stoneValue,prev_X, i):
            if i>= SZ:
                return 0

            if dp[prev_X][i]>-float('inf'): 
                return dp[prev_X][i]
            
            res = -float('inf')
            for X in range(1,4):
                if i+X>SZ: break
                res = max(
                    res, 
                    sum(stoneValue[i:i+X]) - 
                    searching(stoneValue,X, i+X)
                )
            dp[prev_X][i] = res
            return res
        
        diff = searching(stoneValue,1,0)
        for k in [2,3]:
            # if k>=SZ: break
            diff = max(diff, searching(stoneValue, k, 0))

        if diff == 0:
            return 'Tie'
        elif diff > 0:
            return 'Alice'
        else:
            return 'Bob'