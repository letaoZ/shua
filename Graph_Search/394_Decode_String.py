'''
394. Decode String
Medium

7237

306

Add to List

Share
Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; there are no extra white spaces, square brackets are well-formed, etc.

Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there will not be input like 3a or 2[4].

 

Example 1:

Input: s = "3[a]2[bc]"
Output: "aaabcbc"
Example 2:

Input: s = "3[a2[c]]"
Output: "accaccacc"
Example 3:

Input: s = "2[abc]3[cd]ef"
Output: "abcabccdcdcdef"
 

Constraints:

1 <= s.length <= 30
s consists of lowercase English letters, digits, and square brackets '[]'.
s is guaranteed to be a valid input.
All the integers in s are in the range [1, 300].
'''

class Solution:
    def decodeString(self, s: str) -> str:
        #Time Complexity: \mathcal{O}(\text{maxK} ^ {\text{countK}}\cdot n)O(maxK countK⋅n),
        #  where \text{maxK}maxK is the maximum value of kk, 
        # \text{countK}countK is the count of nested kk values 
        # and nn is the maximum length of encoded string. 
        # Example, for s = 20[a10[bc]], \text{maxK}maxK is 2020, 
        # \text{countK}countK is 22 as there are 22 nested kk values (20 and 10) .
        # Also, there are 22 encoded strings a and bc with maximum length of encoded string ,
        # nn as 22

        queue = collections.deque()
        for ss in s:
            if ss !=']':
                queue.append(ss)
                continue
            pss = ""
            while queue:
                ss= queue.pop()
                if ss == '[':
                    break
                pss = ss+pss
            # print(f"pss:{pss}")
            num = ""
            while queue:
                ss = queue.pop()
                if ss in [str(i) for i in range(10)]:
                    num += ss
                    continue
                else:
                    queue.append(ss)
                    break
            if len(num) > 0:
                num = int(num[::-1])
            else:
                num = 1
            queue.append(pss*num)
            # print("queue")
            # print(queue)
            # print()
        res = ""
        while queue:
            res += queue.popleft()
        return res
                

class Solution1:
    def decodeString(self, s: str) -> str:
        
        if not s: return s
        q = collections.deque()
        nums = [str(i) for i in range(10)]
        for ss in s:
            if ss != ']':
                q.append(ss)
                continue
                
            rep = []
            while q and q[-1]!='[':
                rep.append(q.pop())
            q.pop()
            rep = rep[::-1]
            rep = "".join(rep)
            num = ""
            while q and q[-1] in nums:
                num += q.pop()
            num = int(num[::-1])
            q.append(num*rep)
        return "".join(q)
        
        
class Solution1:
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """        
        ## if there is a number, there is at least 4 letters
        if len(s) <=2: return s
        i = 1
        stack = collections.deque() 
        ## keep on pushing till see ]; 
        ## once we see ], keep on popping till see [

        i = 1
        stack.append(s[0])
        nums = [ str(i) for i in range(10) ]
        while i<len(s):
            while i< len(s) and s[i]!="]":
                stack.append(s[i]); i+= 1
            if i==len(s):
                return "".join(stack)
            ## pop right
            tmp = ""
            while stack and stack[-1] !="[": 
                tmp = stack.pop() + tmp
            if stack: stack.pop()
            ntmp = ""
            while stack and  stack[-1] in nums: ntmp = stack.pop()  + ntmp
            stack.append(int(ntmp)* tmp)
            i += 1
        return "".join(stack)
        

class Solution1:
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """        
        stack  = collections.deque()
        numbs   = [str(k) for k in range(10)]
        i = len(s) - 1
        tmp = ""
        
        while i >= 0:
            if s[i]!='[': 
                stack.appendleft(s[i])
                i -= 1
                continue
            mult = ""
            while i-1 >= 0 and (s[i-1] in numbs):
                mult =  s[i-1]  + mult
                i -= 1
            tmp = ""
            while stack and stack[0]!="]":
                ##注意加的顺序，这里和之前不同
                ## 是从stack里走，所以是tmp + stack[0]
    
                tmp =  tmp + stack[0]
                stack.popleft()
            if stack[0] == "]": stack.popleft()
                
            stack.appendleft(tmp*(int(mult)))
            i -= 1
        
        return "".join(stack)
                