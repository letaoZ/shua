'''
1073. Adding Two Negabinary Numbers
Medium

Given two numbers arr1 and arr2 in base -2, return the result of adding them together.

Each number is given in array format:  as an array of 0s and 1s, from most significant bit to least significant bit.  For example, arr = [1,1,0,1] represents the number (-2)^3 + (-2)^2 + (-2)^0 = -3.  A number arr in array, format is also guaranteed to have no leading zeros: either arr == [0] or arr[0] == 1.

Return the result of adding arr1 and arr2 in the same format: as an array of 0s and 1s with no leading zeros.

 

Example 1:

Input: arr1 = [1,1,1,1,1], arr2 = [1,0,1]
Output: [1,0,0,0,0]
Explanation: arr1 represents 11, arr2 represents 5, the output represents 16.
Example 2:

Input: arr1 = [0], arr2 = [0]
Output: [0]
Example 3:

Input: arr1 = [0], arr2 = [1]
Output: [1]
 

Constraints:

1 <= arr1.length, arr2.length <= 1000
arr1[i] and arr2[i] are 0 or 1
arr1 and arr2 have no leading zeros
'''



class Solution:
    def addNegabinary_scan_one_by_one(self, arr1: List[int], arr2: List[int]) -> List[int]:
        ## make even odd addition

        dp_binary = {1:[1]}
        def get_binary(k):## reversed binary
            if k in dp_binary:
                return dp_binary[k]
            
            if k == 0:
                return []
            res = [k%2]
            
            res.extend(get_binary(k//2) )
            dp_binary[k] = res
            return res
        
        ## idea:
        ## first get binary expression, then check all odd nonzero digit
        nbinaries = {0:[0]} ## reversed neg binary
        
        def get_nbinary(k):
            if k in nbinaries:
                return nbinaries[k]
            
            ## odd digit  + 2  // 2
            cnt = 0
            res = []
            
            ## first transform the number to positive
            ## this is like shift digit
            if k<0:
                if k % 2 == 1:
                    res.append(1)
                    k -= 1
                k = k//(-2)                    
            while k>0:
                # print(k)
                # print(res)
                if cnt % 2 == 0: ## normal case
                    res.append(k % 2)
                    k = k//2
                elif cnt % 2 != 0: ## need more consideration
                    if k % 2 == 0:
                        res.append(0)
                        k = k//2
                    else:
                        res.append(1)
                        k = (k + 2)//2
                cnt += 1
            nbinaries[k] = res
            return res

        ## when we roll up the digits,
        ## we need to consider what we get in res[d]
        
        i1, i2 = len(arr1) - 1, len(arr2) - 1
        res = [0]*3000 ## just to make enough space
        len_res = 0
        d = 0
        while i1 >= 0 or i2 >= 0:
            s = res[d]
            if i1>=0:
                s += arr1[i1]
                i1 -= 1
            if i2 >=0:
                s+= arr2[i2]
                i2 -= 1
            if s<2:
                res[d] = s
                s = 0
                
            elif s >= 2: ## we garantee that s is at most 3
                reversed_nbinary = get_nbinary(s)
                # print(s)
                # print(reversed_nbinary)
                res[d] = 0
                for i,v in enumerate(reversed_nbinary):
                    res[d+i] += v
                len_res = max(len_res, d + len(reversed_nbinary))
            d += 1
            len_res = max(d, len_res)
        res = res[:len_res]
        for i in range(len(res)-1):
            if res[i] == res[i+1]*2  :
                res[i] = res[i+1] = 0
        res = res[::-1]
        i = 0
        while i<len(res) and res[i] == 0:
            i += 1
            
        if i == len(res):
            return [0]
        else:
            return res[i:]
        
    def addNegabinary(self, arr1: List[int], arr2: List[int]) -> List[int]:
        ## make even odd addition
        
        ## idea:
        ## first get binary expression, then check all odd nonzero digit
        nbinaries = {(1,0):[0], (0,0):[0]} ## reversed neg binary
        
        def get_nbinary( cnt, k ):
            if (cnt,k) in nbinaries:
                return nbinaries[(cnt,k)]
            
            ## odd digit  + 2  // 2
            res = []
            
            ## first transform the number to positive
            ## this is like shift digit
            if cnt == 0: ## normal case
                res.append(k % 2)
                k = k//2
                res.extend(get_nbinary(1,k) )
            if cnt == 1: ## need more consideration
                if k % 2 == 0:
                    res.append(0)
                    k = k//2
                else:
                    res.append(1)
                    k = (k + 2)//2
                res.extend(get_nbinary(0,k))

            nbinaries[k] = res
            return res
        
        
        ## when we roll up the digits,
        ## we need to consider what we get in res[d]
        
        i1, i2 = len(arr1) - 1, len(arr2) - 1
        res = [0]*(len(arr1) + len(arr2))*2 ## just to make enough space
        len_res = 0
        d = 0
        while i1 >=0 or i2 >= 0:
            if i1>=0:
                res[d] += arr1[i1]
                i1 -= 1
            if i2 >=0:
                res[d]+= arr2[i2]
                i2 -= 1
            ## run cancellation
            if d>0:
                a = res[d-1]//2
                b = res[d]
                if a <= b:
                    res[d] = b-a
                    res[d-1] = res[d-1] % 2
                elif a>b:
                    res[d] = 0
                    res[d-1] = res[d-1] - 2*b
            d += 1
        if set(res) == set([0]):
            return [0]
        len_res = d
        d = 0
        L = len_res+1
        
        for d in range(len_res+1):
            # print(res[:len_res])
            s = res[d]
            if s<2:
                continue
                
            elif s >= 2: ## we garantee that s is at most 3
                reversed_nbinary = get_nbinary(0, s)
                # print(s)
                # print(reversed_nbinary)
                res[d] = 0
                for i,v in enumerate(reversed_nbinary):
                    res[d+i] += v
                L = max(d+len(reversed_nbinary),L)
                
        res = res[:L]
        for i in range(len(res)-1):
            if res[i] == res[i+1]*2  :
                res[i] = res[i+1] = 0
        res = res[::-1]
        i = 0
        while i<len(res) and res[i] == 0:
            i += 1
            
        if i == len(res):
            return [0]
        else:
            return res[i:]