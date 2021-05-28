'''1690. Stone Game VII
Medium

Alice and Bob take turns playing a game, with Alice starting first.

There are n stones arranged in a row. On each player's turn, they can remove either the leftmost stone or the rightmost stone from the row and receive points equal to the sum of the remaining stones' values in the row. The winner is the one with the higher score when there are no stones left to remove.

Bob found that he will always lose this game (poor Bob, he always loses), so he decided to minimize the score's difference. Alice's goal is to maximize the difference in the score.

Given an array of integers stones where stones[i] represents the value of the ith stone from the left, return the difference in Alice and Bob's score if they both play optimally.

 

Example 1:

Input: stones = [5,3,1,4,2]
Output: 6
Explanation: 
- Alice removes 2 and gets 5 + 3 + 1 + 4 = 13 points. Alice = 13, Bob = 0, stones = [5,3,1,4].
- Bob removes 5 and gets 3 + 1 + 4 = 8 points. Alice = 13, Bob = 8, stones = [3,1,4].
- Alice removes 3 and gets 1 + 4 = 5 points. Alice = 18, Bob = 8, stones = [1,4].
- Bob removes 1 and gets 4 points. Alice = 18, Bob = 12, stones = [4].
- Alice removes 4 and gets 0 points. Alice = 18, Bob = 12, stones = [].
The score difference is 18 - 12 = 6.
Example 2:

Input: stones = [7,90,5,1,100,10,10,2]
Output: 122
 

Constraints:

n == stones.length
2 <= n <= 1000
1 <= stones[i] <= 1000

'''

### NOTE: bob is trying to minimize alice-bob... so he is to maximize bob - alice... stupid!!

class Solution:
    def stoneGameVII_bottomUP(self, stones: List[int]) -> int:
        SZ = len(stones)
        psum = [0]*(SZ+1)
        
        ## psum[i] = sum(stones[:i])
        for i in range(SZ):
            psum[i+1] = psum[i]+stones[i]
        dp =[[0]*(SZ+1) for _ in range(SZ+1)]

        
        for L in range(SZ):
            
            for i in range(SZ-L):
                j = i+L
                dp[i][j] = max(
                    psum[j+1] - psum[i+1] - dp[i+1][j],  
                    psum[j] - psum[i]  - dp[i][j-1])
        return dp[0][SZ-1]

        
    def stoneGameVII_topdown_dp_mem(self, stones: List[int]) -> int:
        SZ = len(stones)
        psum = [0]*(SZ+1)
        
        ## psum[i] = sum(stones[:i])
        for i in range(SZ):
            psum[i+1] = psum[i]+stones[i]
            
            
        dp =[[-1]*SZ for _ in range(SZ)]
        
        
        def searching(stones, x,y):
            if x>=y or x<0 or y>=SZ:
                return 0
            
            if dp[x][y]>=0:
                return dp[x][y]
            
            
            res = max(psum[y+1] - psum[x+1] -searching(stones,x+1,y), 
                         psum[y] -psum[x]- searching(stones,x,y-1))

            dp[x][y] = res
            return res
                
            
        diff = searching(stones, 0,SZ-1)

        return diff