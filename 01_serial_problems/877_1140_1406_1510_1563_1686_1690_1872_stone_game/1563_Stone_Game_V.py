'''1563. Stone Game V
Hard


There are several stones arranged in a row, and each stone has an associated value which is an integer given in the array stoneValue.

In each round of the game, Alice divides the row into two non-empty rows (i.e. left row and right row), then Bob calculates the value of each row which is the sum of the values of all the stones in this row. Bob throws away the row which has the maximum value, and Alice's score increases by the value of the remaining row. If the value of the two rows are equal, Bob lets Alice decide which row will be thrown away. The next round starts with the remaining row.

The game ends when there is only one stone remaining. Alice's is initially zero.

Return the maximum score that Alice can obtain.

 

Example 1:

Input: stoneValue = [6,2,3,4,5,5]
Output: 18
Explanation: In the first round, Alice divides the row to [6,2,3], [4,5,5]. The left row has the value 11 and the right row has value 14. Bob throws away the right row and Alice's score is now 11.
In the second round Alice divides the row to [6], [2,3]. This time Bob throws away the left row and Alice's score becomes 16 (11 + 5).
The last round Alice has only one choice to divide the row which is [2], [3]. Bob throws away the right row and Alice's score is now 18 (16 + 2). The game ends because only one stone is remaining in the row.
Example 2:

Input: stoneValue = [7,7,7,7,7,7,7]
Output: 28
Example 3:

Input: stoneValue = [4]
Output: 0
 

Constraints:

1 <= stoneValue.length <= 500
1 <= stoneValue[i] <= 10^6

'''


class Solution:
    def stoneGameV(self, A):
        n = len(A)
        prefix = [0] * (n + 1)
        for i, a in enumerate(A):
            prefix[i + 1] = prefix[i] + A[i]

        @functools.lru_cache(None)
        def dp(i, j):
            if i == j: return 0
            res = 0
            for m in range(i, j):
                left = prefix[m + 1] - prefix[i]
                right = prefix[j + 1] - prefix[m + 1]
                if left <= right:
                    res = max(res, dp(i, m) + left)
                if left >= right:
                    res = max(res, dp(m + 1, j) + right)
            return res
        return dp(0, n - 1)
    
    def stoneGameV_slow_becauseOfDP(self, stones: List[int]) -> int:
        '''
         This was one such question where the fact that "tabular dp runs through all possible states even if we would never encounter it in recuresive dp" is exploited. But we can also not deny the fact that recursive dp is more time consuming in general. But in this question we are just ignoring most of the states just by checking its range sum, so it makes the recursive approach faster. Trade off !
Good play by the setter, but was it intentional or a testing blunder. Never know.
'''

        sz = len(stones)
        dp = [ [-float('inf')]*sz for _ in range(sz) ]
        psum = [0]*(sz + 1)
        for i,n in enumerate(stones):
            psum[i+1] = psum[i]+stones[i]
            
        def searching(stones,x,y, dp):
            if x>=y:
                return 0
            if dp[x][y]>-float('inf'):
                return dp[x][y]
            
            res_all = -float('inf')
            for k in range(x,y):
                res = -float('inf')
                sumL = psum[k+1] - psum[x] ##sum(stones[x:k+1])
                sumR = psum[y+1] - psum[k+1] ##sum(stones[k+1:y+1])
                if sumL >= sumR:
                    res = sumR + searching(stones,k+1,y,dp)
                if sumL<=sumR:
                    res = sumL + searching(stones, x,k,dp)
                # else:
                #     res = sumL + max(searching(stones,k+1,y,dp), searching(stones, x,k,dp))
                res_all = max(res, res_all)
        
            
            dp[x][y] = res_all
            return res_all
        res = searching(stones,0,sz-1,dp)

        return res
        
                
