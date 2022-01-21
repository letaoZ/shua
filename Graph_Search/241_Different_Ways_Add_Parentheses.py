'''
241. Different Ways to Add Parentheses
Medium

3178

160

Add to List

Share
Given a string expression of numbers and operators, return all possible results from computing all the different possible ways to group numbers and operators. You may return the answer in any order.

 

Example 1:

Input: expression = "2-1-1"
Output: [0,2]
Explanation:
((2-1)-1) = 0 
(2-(1-1)) = 2
Example 2:

Input: expression = "2*3-4*5"
Output: [-34,-14,-10,-10,10]
Explanation:
(2*(3-(4*5))) = -34 
((2*3)-(4*5)) = -14 
((2*(3-4))*5) = -10 
(2*((3-4)*5)) = -10 
(((2*3)-4)*5) = 10
 

Constraints:

1 <= expression.length <= 20
expression consists of digits and the operator '+', '-', and '*'.
All the integer values in the input expression are in the range [0, 99].
'''
class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        ## num op num --> num
        ## Catalan number as time complexity
        ## stirling: n!~ sqrt(2pi n) (n/e)^n
        
        res = []
        expr = []
        i = 0
        nums = [str(_) for _ in range(10)]
        while i< len(expression):
            n = ''
            j = i
            while j<len(expression) and expression[j] in nums:
                n += expression[j]
                j += 1
            
            if len(n) > 0:
                expr.append(n)
            if j<len(expression):
                expr.append(expression[j])
            i = j + 1
        ops = ['+', '-', '*']
        
        op_map = {
            "+": (lambda x,y: x + y),
            "-": (lambda x,y: x - y),
            "*": (lambda x,y: x * y),

        }
        
        computed = {}
        def compute_expr(expr):
            
            if len(expr) <= 1:
                return expr

            res = []
            for i, op in enumerate(expr):
                if op not in ops:
                    continue
                if tuple(expr[:i]) in computed:
                    left_values = computed[tuple(expr[:i])]
                else:
                    left_values = compute_expr(expr[:i])
                    computed[tuple(expr[:i])] = left_values
                if tuple(expr[i+1:]) in computed:
                    right_values = computed[tuple(expr[i+1:])]
                else:
                    right_values = compute_expr(expr[i+1:])
                    computed[tuple(expr[i+1:])] = right_values
                for pl in left_values:
                    for pr in right_values:
                        res.append(op_map[op](int(pl),int(pr) ) )
                        
                        
                        
            return res
        
        
        res = compute_expr(expr)
        return res