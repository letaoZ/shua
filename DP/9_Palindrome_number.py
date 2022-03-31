'''
9. Palindrome Number
Easy

5474

2075

Add to List

Share
Given an integer x, return true if x is palindrome integer.

An integer is a palindrome when it reads the same backward as forward.

For example, 121 is a palindrome while 123 is not.
 

Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
 

Constraints:

-231 <= x <= 231 - 1
'''

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x == 0: return True

        if x<0 or (10* (x//10) == x): return False
        rev_sum = 0
        while(x>rev_sum):
            rev_sum = (x%10 + rev_sum*10)
            x //= 10
        ## even odd
        return (rev_sum == x) or (rev_sum // 10 == x)

    def isPalindrome_all(self, x: int) -> bool:
        if x<0: return False
        rev_sum = 0
        r = x
        while(r>0):
            rev_sum = (r%10 + rev_sum*10)
            r //= 10
        p
        return (rev_sum == x)
        
        
    def isPalindrome_str(self, x: int) -> bool:
        if x<0: return False
        sx = str(x)
        l, r = 0, len(sx)-1
        while (l<r):
            if sx[l]!=sx[r]: return False
            l += 1
            r -= 1
        return True