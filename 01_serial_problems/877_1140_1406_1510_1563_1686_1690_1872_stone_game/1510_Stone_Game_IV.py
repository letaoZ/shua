'''1510. Stone Game IV
Alice and Bob take turns playing a game, with Alice starting first.

Initially, there are n stones in a pile.  On each player's turn, that player makes a move consisting of removing any non-zero square number of stones in the pile.

Also, if a player cannot make a move, he/she loses the game.

Given a positive integer n. Return True if and only if Alice wins the game otherwise return False, assuming both players play optimally.

 

Example 1:

Input: n = 1
Output: true
Explanation: Alice can remove 1 stone winning the game because Bob doesn't have any moves.
Example 2:

Input: n = 2
Output: false
Explanation: Alice can only remove 1 stone, after that Bob removes the last one winning the game (2 -> 1 -> 0).
Example 3:

Input: n = 4
Output: true
Explanation: n is already a perfect square, Alice can win with one move, removing 4 stones (4 -> 0).
Example 4:

Input: n = 7
Output: false
Explanation: Alice can't win the game if Bob plays optimally.
If Alice starts removing 4 stones, Bob will remove 1 stone then Alice should remove only 1 stone and finally Bob removes the last one (7 -> 3 -> 2 -> 1 -> 0). 
If Alice starts removing 1 stone, Bob will remove 4 stones then Alice only can remove 1 stone and finally Bob removes the last one (7 -> 6 -> 2 -> 1 -> 0).
Example 5:

Input: n = 17
Output: false
Explanation: Alice can't win the game if Bob plays optimally.
Constraints:

1 <= n <= 10^5
'''

class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        dp = [-1]*(n+1)
        dp[0] = 0
        for num in range(0, n+1):
            
            ## if with num many stones left means win, 
            # then the extra j^2 means the other person
            ## took the last stone
            
            ## Try all possible square numbers and see whether the other player 
            ## will lose or not.
            ## win(n) = any(win(n – i*i) == False) ? True : False
            if dp[num] == 1: continue
            bound = int(  (n-num)**0.5 )
            for j in range(1,bound + 1):
                dp[num + j**2] = 1
        return (dp[n]==1)
    
    def winnerSquareGame_topdown_dp(self, n: int) -> bool:
        ## time N^(sqrt(N))
        def searching(num, dp):
            if dp[num]!=-1:
                return (dp[num] == 1)
            
            bound = int(num**(0.5))
            res = False
            for k in range(1,bound+1):
                res = (not searching(num-k**2, dp) )
                if res:
                    dp[num] = 1
                    return True
            dp[num] = 0
            return False
        
        dp = [-1]*(n+1)
        dp[0] = 0
        dp[1] = 1
        
        res = searching(n, dp)            
            
        return res