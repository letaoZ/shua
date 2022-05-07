'''
1209. Remove All Adjacent Duplicates in String II
Medium

3490

67

Add to List

Share
You are given a string s and an integer k, a k duplicate removal consists of choosing k adjacent and equal letters from s and removing them, causing the left and the right side of the deleted substring to concatenate together.

We repeatedly make k duplicate removals on s until we no longer can.

Return the final string after all such duplicate removals have been made. It is guaranteed that the answer is unique.

 

Example 1:

Input: s = "abcd", k = 2
Output: "abcd"
Explanation: There's nothing to delete.
Example 2:

Input: s = "deeedbbcccbdaa", k = 3
Output: "aa"
Explanation: 
First delete "eee" and "ccc", get "ddbbbdaa"
Then delete "bbb", get "dddaa"
Finally delete "ddd", get "aa"
Example 3:

Input: s = "pbbcggttciiippooaais", k = 2
Output: "ps"
 

Constraints:

1 <= s.length <= 105
2 <= k <= 104
s only contains lower case English letters.
'''

class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        cnt = [['#',0]]
        for e in s:
            if cnt[-1][0] != e:
                cnt.append([e,1])
            elif cnt[-1][0] == e:
                if cnt[-1][1] == k-1:
                    cnt.pop()
                else:
                    cnt[-1][1] += 1
                    
        print(self.removeDuplicates_kmore(s,k))
        return "".join([a for a,b in cnt[1:]])
    def removeDuplicates_kmore(self, s: str, k: int) -> str:
        ## left-to-right removal order
        cnt = [['#',0]]
        
        i = 0
        while i< len(s):
            e = s[i]
            if cnt[-1][0] != e:
                cnt.append([e,1])
                i += 1
            elif cnt[-1][0] == e:
                while cnt[-1][0] == e:
                    cnt[-1][1] += 1
                    i += 1
                    if i < len(s):
                        e = s[i]
                    else:
                        break
                if cnt[-1][1] >= k:
                    cnt.pop()
                    
        
        return "".join([a for a,b in cnt[1:]])


    def removeDuplicates_kmore(self, s: str, k: int) -> str:
        
        
        def dfs(s,  res):
            if res[1] > len(s):
                res[0] = s
                res[1] = len(s)
            
            cnt = [['#',0]]
            i = 0
            while i<len(s):
                
                e = s[i]
                if cnt[-1][0] != e:
                    cnt.append([e,1])
                    i += 1
                elif cnt[-1][0] == e:
                    while cnt[-1][0] == e:
                        cnt[-1][1] += 1
                        i += 1
                        if i < len(s):
                            e = s[i]
                        else:
                            break
                    if cnt[-1][1] >= k:
                        pre_s = "".join([a for a,b in cnt[1:]])
                        after_s = s[i:]
                        dfs(pre_s + after_s,  res)

        res = ["#",len(s)+1]
        dfs(s,res)