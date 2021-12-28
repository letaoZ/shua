
'''
72. Edit Distance
Hard

7287

86

Add to List

Share
Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.

You have the following three operations permitted on a word:

Insert a character
Delete a character
Replace a character
 

Example 1:

Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation: 
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')
Example 2:

Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation: 
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')
 

Constraints:

0 <= word1.length, word2.length <= 500
word1 and word2 consist of lowercase English letters.
'''



class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        if len(set(word1).intersection(set(word2))) == 0:
            return max(len(word1),len(word2))
        
        # if s1[i] == s2[j]:
        #     啥都别做（skip）
        #     i, j 同时向前移动
        # else:
        #     三选一：
        #         插入（insert）
        #         删除（delete）
        #         替换（replace）
        
        ##  定义：dp(i, j) 返回 s1[0..i] 和 s2[0..j] 的最小编辑距离
        def searching(word1, word2, i,j):
            
            if i<0:
                return j+1
            if j<0:
                return i+1
            if word1[i] == word2[j]:
                return searching(word1, word2, i-1,j-1)
            
            if dp[i][j]<float('inf'):
                return dp[i][j]
            
            
            
            dp[i][j] = min(searching(word1, word2, i, j-1) + 1, ## insert word1 with word2[j] 
                           searching(word1, word2, i-1, j) + 1, ## delete word1[i]
                            searching(word1, word2, i-1, j-1) + 1, ## replace word1[i] with word2[j]
                          )
            return dp[i][j]
        
        dp = [ [float('inf')]*(len(word2)) for _ in range(len(word1))]
        
        dp[0][0] = int(word1[0] != word2[0])
        
        return searching(word1, word2, len(word1)-1, len(word2)-1)