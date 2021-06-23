'''403. Frog Jump


A frog is crossing a river. The river is divided into some number of units, 
and at each unit, there may or may not exist a stone. The frog can jump on a stone, 
but it must not jump into the water.

Given a list of stones' positions (in units) in sorted ascending order, 
determine if the frog can cross the river by landing on the last stone. 
Initially, the frog is on the first stone and assumes the first jump must be 1 unit.

If the frog's last jump was k units, its next jump must be either k - 1, k, or k + 1 units. The frog can only jump in the forward direction.

 

Example 1:

Input: stones = [0,1,3,5,6,8,12,17]
Output: true
Explanation: The frog can jump to the last stone by jumping 1 unit to the 2nd stone, then 2 units to the 3rd stone, then 2 units to the 4th stone, then 3 units to the 6th stone, 4 units to the 7th stone, and 5 units to the 8th stone.
Example 2:

Input: stones = [0,1,2,3,4,8,9,11]
Output: false
Explanation: There is no way to jump to the last stone as the gap between the 5th and 6th stone is too large.
 

Constraints:

2 <= stones.length <= 2000
0 <= stones[i] <= 231 - 1
stones[0] == 0

'''


List = list()
class Solution:
    def canCross(self, stones: List[int]) -> bool:
        sz = len(stones)
        dp = [ [0]*(sz+1) for _ in range(sz+1)] ## whether we can reach dp[i] stones[i]
        if stones[0]!=0:
            return False
        ## at stone[i], dp[i][k] == 1 means you can move k steps from stone[i]
        # dp[0][0] = 1
        dp[0][1] = 1
        for i in range(1, sz):
            for j in range(i):
                d = stones[i] - stones[j]
                
                if d>i+1: continue
                if d<0: continue
                if dp[j][d] == 0: continue
                    
                dp[i][d] = 1
                if d>=1:
                    dp[i][d-1] = 1
                if d+1<= sz:
                    dp[i][d+1] = 1
                if i == sz-1:
                    return True
        return False


    def canCross_topdown_no_mem(self, stones: List[int]) -> bool:
        if stones[0]!=0:
            return False
        if len(stones) > 0 and stones[1]!=1:
            return False
        
        sz = len(stones)
        visited = [[0]*(len(stones)+2) for _ in range(len(stones))]
        visited[0][0] = visited[1][1] = 1
        
        
        def searching(i,k):
            

            if i == sz-1:
                return True
            val = stones[i]
            # visited[i][k] = 1
            for delta_k in [k-1, k, k+1]:
                valn = delta_k + val
                for j in range(i+1, sz):
                    if stones[j]>valn:
                        break
                    if stones[j] == valn and searching(j, delta_k):
                        
                        return True
            return False
        
        res = searching(1,1)
        
        
        return (res)