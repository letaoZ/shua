'''
29. Divide Two Integers
Medium

3283

11155

Add to List

Share
Given two integers dividend and divisor, divide two integers without using multiplication, division, and mod operator.

The integer division should truncate toward zero, which means losing its fractional part. For example, 8.345 would be truncated to 8, and -2.7335 would be truncated to -2.

Return the quotient after dividing dividend by divisor.

Note: Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: [−231, 231 − 1]. For this problem, if the quotient is strictly greater than 231 - 1, then return 231 - 1, and if the quotient is strictly less than -231, then return -231.

 

Example 1:

Input: dividend = 10, divisor = 3
Output: 3
Explanation: 10/3 = 3.33333.. which is truncated to 3.
Example 2:

Input: dividend = 7, divisor = -3
Output: -2
Explanation: 7/-3 = -2.33333.. which is truncated to -2.
 

Constraints:

-231 <= dividend, divisor <= 231 - 1
divisor != 0

'''

## careful about constraints
from typing import *
class Solution:
    
        
    def divide(self, dividend: int, divisor: int) -> int:
        sign = 1
        if dividend == 0:
            return 0
        if (dividend > 0 and divisor < 0) or (dividend < 0 and divisor > 0):
            sign = -1
            
        dividend = abs(dividend)
        divisor = abs(divisor)
        # print(dividend)
        if dividend < divisor:
            return 0
        
        M = int(2**31 - 1)
        res = 0
        while dividend >= divisor:
            m = 1
            temp = divisor
            while dividend >= (temp << 1):
                m <<= 1
                temp <<= 1
            dividend -= temp
            res += m
            # print(res)
        
        res = -res if sign == -1 else res
        if res < 0:
            res = max(res, - (M + 1))
        else:
            res = min(M, res)
        
        return res
            
            