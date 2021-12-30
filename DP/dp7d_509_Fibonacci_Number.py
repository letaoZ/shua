'''
509. Fibonacci Number    
Easy

2399

244

Add to List

Share
The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,

F(0) = 0, F(1) = 1
F(n) = F(n - 1) + F(n - 2), for n > 1.
Given n, calculate F(n).

'''

class Solution0:
    def fib(self, n: int) -> int:
        if n<=1:
            return n
        
        n0, n1 = 0, 1
        while n>1:
            n0 = n0 + n1
            n0, n1 = n1, n0
            n -= 1
        
        return n1
    
    
class Solution: 
    ## compute power of matrix method
    def prod_mat(self, mat1, mat2):
        res = [[0,0],[0,0]]
        for i in range(2):
            for k in range(2):
                res[i][k] = sum([mat1[i][j]*mat2[j][k] for j in range(2)] )
        return res
    
    def power(self, x, n):
        # Initialize result
        res = [[1,0],[0,1]]

        while (n > 0):
            # If y is odd, multiply
            # x with result
            if ((n & 1) == 1) :
                res = self.prod_mat(x, res)


            # now n = n/2
            n = n >> 1

            # Change res to res^2
            x = self.prod_mat(x,x)

        return res
    def power1(self,x, y):
 
        # Initialize result
        res = 1

        while (y > 0):

            # If y is odd, multiply
            # x with result
            if ((y & 1) == 1) :
                res = res * x

            # y must be even
            # now y = y/2
            y = y >> 1

            # Change x to x^2
            x = x * x
    
        return res
    def fib(self, n: int) -> int:
        if n<=1:
            return n
        
        trans_mat = [[0,1],[1,1]]
        
        # (a1,a2)^t = trans_mat* (a0,a1)^t
        power_mat = self.power(trans_mat, n-1)
        
        res = power_mat[1][1]
        print(power_mat)
        return res