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
        ## either remove left or right, depends on s
        ## consider remove right first

        
        def build_parentheses(s, leftp = "(", rightp = ")"):
            res = [""]
            N = len(s)
            left_cnt = 0
            right_cnt = 0
            right_idx = []

            i = 0
            while i < N:
                if s[i] not in [leftp, rightp]:#["(",")"]:
                    pass
                elif s[i] == leftp:#"(":
                    left_cnt += 1
                elif s[i] == rightp:#")":
                    right_cnt += 1

                if left_cnt >= right_cnt:
                    for ii in range(len(res)):
                        res[ii] += s[i] 
                else: ## remove a right p
                    cur_res = [ _ for _ in res] ## expression without new rightp added
                    for ll in res: ## start removing the extra ")", and add the new rightp at the end
                        for il,vl in enumerate(ll):
                            if vl == rightp: #")":
                                tmpl = ll[:il] + ll[il+1:] + rightp #")"
                                if tmpl not in cur_res:
                                    cur_res.append(tmpl)
                    res = [_ for _ in cur_res]
                    right_cnt -= 1
                i += 1
            return left_cnt, right_cnt, res
        
        left_cnt, right_cnt, left_res = build_parentheses(s)
        if left_cnt == right_cnt:
            return left_res
        # print(left_res)
        res = []
        for sl in left_res:
            left_cnt, right_cnt, right_res = build_parentheses(sl[::-1],")", "(")
            # print("left_cnt, right_cnt",left_cnt, right_cnt)
            right_res = [ll[::-1] for ll in right_res]
            # print(right_res)
            if left_cnt == right_cnt:
                for kk in right_res:
                    if kk not in res:
                        res.append(kk)

        return res if res else [""]
        
        
        