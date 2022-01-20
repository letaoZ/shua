'''
679. 24 Game
Hard

1113

205

Add to List

Share
You are given an integer array cards of length 4. You have four cards, each containing a number in the range [1, 9]. You should arrange the numbers on these cards in a mathematical expression using the operators ['+', '-', '*', '/'] and the parentheses '(' and ')' to get the value 24.

You are restricted with the following rules:

The division operator '/' represents real division, not integer division.
For example, 4 / (1 - 2 / 3) = 4 / (1 / 3) = 12.
Every operation done is between two numbers. In particular, we cannot use '-' as a unary operator.
For example, if cards = [1, 1, 1, 1], the expression "-1 - 1 - 1 - 1" is not allowed.
You cannot concatenate numbers together
For example, if cards = [1, 2, 1, 2], the expression "12 + 12" is not valid.
Return true if you can get such expression that evaluates to 24, and false otherwise.

 

Example 1:

Input: cards = [4,1,8,7]
Output: true
Explanation: (8-4) * (7-1) = 24
Example 2:

Input: cards = [1,2,1,2]
Output: false
 

Constraints:

cards.length == 4
1 <= cards[i] <= 9


'''

class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        
        
        visited = set()
        eps = 1e-9
        
        def searching(cases):
            if len(cases) == 1:
                if abs(cases[0] - 24.0) < eps:
                    return True
            
            
            for i in range(len(cases)):
                n1 = cases[i]
                for j in range(i):
                    
                    n2 = cases[j]
                    candi =set( [n1+n2, n1-n2, n2 - n1,  n1*n2])#, -n1*n2, -n1-n2] )
                    if abs(n1) > eps:
                        candi.add(n2/n1)
                        # candi.add(-n2/n1)
                    if abs(n2) > eps:
                        candi.add(n1/n2)
                        # candi.add(-n1/n2)
                    
                    new_cases = cases[:j] + cases[j+1:i] + cases[i+1:]
                    
                    for c in candi:
                        res = searching(new_cases + [c])
                        if res:
                            return True

            return False
        return searching(cards)
    
    
    def judgePoint24_simplified(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        ## NOTE: all negative will NOT be a solution anyways
        ## so we don't need to check that
        
        tol = 1e-6
        def dfs(nums, numSize,tol):
            if numSize == 1:
                if 24-tol<nums[0]<24+tol: return True
                else: return False
            a=b=0
            for i in range(1,numSize):
                for j in range(i): ## instead of creating a new list of candidates, we can modify the old slightly
                    a = nums[i]
                    b = nums[j]
                    nums[i] = nums[numSize-1]
                    
                    candi ={a+b, a-b, b-a, a*b}
                    if a>tol: candi.add(b/a)
                    if b>tol: candi.add(a/b)
                    for t in candi:
                        nums[j] = t
                        if dfs(nums,numSize-1,tol): return True
                    nums[i] = a
                    nums[j] = b
            return False
        return dfs(nums,len(nums), tol)
        