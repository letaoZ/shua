'''
301. Remove Invalid Parentheses
Hard

4271

210

Add to List

Share
Given a string s that contains parentheses and letters, remove the minimum number of invalid parentheses to make the input string valid.

Return all the possible results. You may return the answer in any order.

 

Example 1:

Input: s = "()())()"
Output: ["(())()","()()()"]
Example 2:

Input: s = "(a)())()"
Output: ["(a())()","(a)()()"]
Example 3:

Input: s = ")("
Output: [""]
 

Constraints:

1 <= s.length <= 25
s consists of lowercase English letters and parentheses '(' and ')'.
There will be at most 20 parentheses in s.

'''



class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        
        def balance_right(s,leftp = '(', rightp = ')'):
            i = 0
            N = len(s)
            left_p = right_p = 0
            res=['']
            while i<N:
                # print(i)
                if s[i] == rightp:
                    if left_p >= right_p+1: ## valid
                        right_p += 1
                        for ii,l in enumerate(res):
                            res[ii] = l + rightp
                    else:
                        # now we have one extra right_p; we can remove this ) or remove some other previous )
                        new_res = [_ for _ in res]
                        for l in res:
                            for j, e in enumerate(l):
                                if e!=rightp:
                                    continue
                                new_l = l[:j] + l[j+1:] + rightp
                                if new_l not in new_res:
                                    new_res.append(new_l)
                        res = [_ for _ in new_res]

                elif s[i] == leftp:
                    left_p += 1
                    for ii,l in enumerate(res):
                        res[ii] = l + leftp
                else:
                    for ii,l in enumerate(res):
                        res[ii] = l + s[i]
                # print(res)
                # print()
                i += 1
            return res, left_p, right_p
        
        
        res0, left_p ,right_p = balance_right(s,leftp = '(', rightp = ')')

        if left_p <=right_p:
            return res0
        
        final_res = []
        for l in res0:
            
            tmp_res, _, _ =balance_right(l[::-1], ')','(')
            for l in tmp_res:
                l = l[::-1]
                if l not in final_res:
                    final_res.append(l)
        
        return final_res