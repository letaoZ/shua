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

class Solution:
    def fib(self, n: int) -> int:
        if n<=1:
            return n
        
        n0, n1 = 0, 1
        while n>1:
            n0 = n0 + n1
            n0, n1 = n1, n0
            n -= 1
        
        return n1