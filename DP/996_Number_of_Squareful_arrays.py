'''
996. Number of Squareful Arrays
Hard

Given an array A of non-negative integers, the array is squareful if for every pair of adjacent elements, their sum is a perfect square.

Return the number of permutations of A that are squareful.  Two permutations A1 and A2 differ if and only if there is some index i such that A1[i] != A2[i].

 

Example 1:

Input: [1,17,8]
Output: 2
Explanation: 
[1,8,17] and [17,8,1] are the valid permutations.
Example 2:

Input: [2,2,2]
Output: 1
'''










import collections

class Solution:
    def numSquarefulPerms(self, A) -> int:
        
        ## step 1: build graph
        ## time = O(sz**2), space = O(sz**2)
        def sum_sq(a,b):
            tmp = int( (a+b)**0.5 )
            return tmp**2 == (a+b)
        
        sz = len(A)
        if sz <= 0:
            return 0
        
        At = set(A)
        if len(At) == 1:
            return int(sum_sq(A[0],A[0]) )

        
        g = collections.defaultdict(set)
        cnt = collections.Counter(A)
        aa= list(At)
        for i,v in enumerate(aa):
            for w in aa[i:]:
                if v==w and cnt[v]==1: 
                    continue
                if sum_sq(v,w):
                    g[v].add(w)
                    g[w].add(v)
        

        
        
        ## step 2: dfs: O(N!)
        def searching(i,g,szing,cnt,res):
            
            if szing == 1:
                res[0] += 1
                return
            
            for j in g[i]:
                if cnt[j] == 0: continue
                cnt[j] -= 1
                searching(j,g,szing-1,cnt,res)
                cnt[j] += 1
                
        szing = sz 
        res = [0]

        for i in (aa):
            szing = sz
            
            cnt[i] -= 1
            searching(i,g,szing,cnt,res)
            cnt[i] += 1
        return res[0]

solu = Solution()
                
test = [1,3,1]
solu.numSquarefulPerms(test)