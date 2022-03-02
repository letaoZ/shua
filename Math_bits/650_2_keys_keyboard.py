'''
650. 2 Keys Keyboard
Medium

2276

156

Add to List

Share
There is only one character 'A' on the screen of a notepad. You can perform two operations on this notepad for each step:

Copy All: You can copy all the characters present on the screen (a partial copy is not allowed).
Paste: You can paste the characters which are copied last time.
Given an integer n, return the minimum number of operations to get the character 'A' exactly n times on the screen.

 

Example 1:

Input: n = 3
Output: 3
Explanation: Intitally, we have one character 'A'.
In step 1, we use Copy All operation.
In step 2, we use Paste operation to get 'AA'.
In step 3, we use Paste operation to get 'AAA'.
Example 2:

Input: n = 1
Output: 0
 

Constraints:

1 <= n <= 1000
'''


class Solution:
    def minSteps(self, n: int) -> int:
        ## copy (s) then past Ns times get: (Ns*A)-> Ns op (NOTE: the string A is already there, counts as one string; the copy op is "saved" this way)
        ## then copy (Ns*s ) and pas Ns2 times get: (Ns2* (Ns A)) -> Ns2 + 1 op
        ## to get length N: we have Ns1*Ns2 * .. * Nsk = N; op = sum(Nsi+1)
        
        ## prime factors + num of prime factors
        
        np = 0 ## num of primes
        sump = 0
        primes = [1]*(n+1)
        
        k = 2
        num = n
        while n>1 and k<=n:
            if primes[k] == 1:
                for i in range(1,num//k + 1):
                    primes[k*i] = 0
            else:
                k += 1
                continue
                
            if n%k == 0:
                while n and n%k ==0:
                    n = n//k
                    np += 1
                    sump += k
                k += 1
        return sump
                
        
        