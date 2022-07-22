'''
69. Sqrt(x)
Easy

4346

3388

Add to List

Share
Given a non-negative integer x, compute and return the square root of x.

Since the return type is an integer, the decimal digits are truncated, and only the integer part of the result is returned.

Note: You are not allowed to use any built-in exponent function or operator, such as pow(x, 0.5) or x ** 0.5.

 

Example 1:

Input: x = 4
Output: 2
Example 2:

Input: x = 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since the decimal part is truncated, 2 is returned.
 

Constraints:

0 <= x <= 231 - 1
'''
class Solution:
    def mySqrt(self, x: int) -> int:
        
        
        ## NOTE: here we return right
        ##  mid CAN reach right:= l + (r-l+1)//2
        ##  So Right must be updated each time
        ## and Left can be ASSIGNED with value mid
        l, r = -1, x // 2 + 1
        while l < r:
            mid = l + (r - l + 1) // 2
            
            m2 = mid ** 2
            if m2 <= x:
                l = mid
                
            else:
                r = mid - 1
                
        return r
            
