'''
remove K or more consecutive letters and find the shortest string after the removal

e.g. K = 3, aaabbbac --> c

'''

class Solution:
    def removeDuplicates_kmore(self, s: str, k: int) -> str:
        ## remove all possible combos
        def dfs(s,  res):
            print("ss: ", s)
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
                    # print("cnt: ", cnt)
                elif cnt[-1][0] == e:
                    while cnt[-1][0] == e:
                        cnt[-1][1] += 1
                        i += 1
                        if i < len(s):
                            e = s[i]
                        else:
                            break
                    # print("cnt: ", cnt)
                    if cnt[-1][1] >= k:
                        pre_s = s[:i-cnt[-1][1]] + s[i:]
                        dfs(pre_s ,  res)

        res = ["#",len(s)+1]
        dfs(s,res)
        return res[0]