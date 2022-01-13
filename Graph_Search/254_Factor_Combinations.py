class Solution:
    def getFactors(self, n: int) -> List[List[int]]:
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
    
    
    
    
    def getFactors(self, n: int) -> List[List[int]]:
        
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