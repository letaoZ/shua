import functools
import collections



class Solution:
    def minDifficulty_bottomUp_mem_2d(self, jobDifficulty, D):
        N = len(jobDifficulty);
        if(N < D):
            return -1;
        dp = [ [0]*N for _ in range(D)];

        dp[0][0] = jobDifficulty[0];
        for j in range(1,N):
            dp[0][j] = max(jobDifficulty[j], dp[0][j - 1]);
        

        for d in range(1,D):
            for l in range(d,N):
                localMax = jobDifficulty[l];
                dp[d][l] = float('inf');
                for schedule in range(l, d-1,-1):
                    localMax = max(localMax, jobDifficulty[schedule]);
                    dp[d][l] = min(dp[d][l], dp[d - 1][schedule - 1] + localMax);
                

        return dp[D - 1][N - 1];

    def minDifficulty_topdown(self, A, d):
        n = len(A)
        if n < d: return -1

        @functools.lru_cache(None)
        def dfs(i, d):
            if d == 1:
                return max(A[i:])
            res, maxd = float('inf'), 0
            for j in range(i, n - d + 1):
                maxd = max(maxd, A[j])
                res = min(res, maxd + dfs(j + 1, d - 1))
            return res
        return dfs(0, d)

jobDifficulty = [6,5,4,3,2,1]
d = 2
solu = Solution()
solu.minDifficulty(jobDifficulty, d)