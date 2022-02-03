'''
254. Factor Combinations
Medium

841

Numbers can be regarded as the product of their factors.

For example, 8 = 2 x 2 x 2 = 2 x 4.
Given an integer n, return all possible combinations of its factors. You may return the answer in any order.

Note that the factors should be in the range [2, n - 1].

 

Example 1:

Input: n = 1
Output: []
Example 2:

Input: n = 12
Output: [[2,6],[3,4],[2,2,3]]
Example 3:

Input: n = 37
Output: []
 

Constraints:

1 <= n <= 107
'''

class Solution:
    def getFactors(self, n: int) -> List[List[int]]:
        ## too slow
        res = []
        
        factors = {}
        def dfs(k,trace, res):
            bound = 2 if not trace else trace[-1]
            for f in range(bound,int(k**0.5)+1):
                
                if k%f == 0:
                    trace.append(f)
                    dfs(k//f,trace,res)
                    res.append([_ for _ in trace] + [k//f])
                    trace.pop()
        
        dfs(n,[],res)
        return res
            
            
    def getFactors_t(self, n: int) -> List[List[int]]:
        ## number itself is not a factor
        if n<=3:
            return []
        res = []
        
        def searching(cur, i):
            # print(f"searching cur: {cur}")
            # print(f"factor: {i}")
            if not cur:
                return
            
            num = cur.pop()
            while i*i <= num:
                if num%i == 0:
                    div = num // i
                    res.append(cur + [i,div])
                    searching(cur+[i, div], i)
                i += 1
            # print("done while cur: ",cur)
            # print()
        searching([n],2)
        return res
    
    
    
    
    def getFactorst(self, n: int) -> List[List[int]]:
        
        ## find factors of N when start at start
        def helper(N,start,out):
            for fac in range(start,int(math.sqrt(N))+1):
                if N % fac == 0:
                    new_out = [j for j in out] ## deep copy
                    new_out.append(fac)
                    helper(N//fac,fac,new_out)
                    new_out.append(N//fac)
                    res.append(new_out)
        
        res = []
        out = []
        helper(n,2,out)
                    
        return res