'''
712. Minimum ASCII Delete Sum for Two Strings
Medium

1717

61

Add to List

Share
Given two strings s1 and s2, return the lowest ASCII sum of deleted characters to make two strings equal.

 

Example 1:

Input: s1 = "sea", s2 = "eat"
Output: 231
Explanation: Deleting "s" from "sea" adds the ASCII value of "s" (115) to the sum.
Deleting "t" from "eat" adds 116 to the sum.
At the end, both strings are equal, and 115 + 116 = 231 is the minimum sum possible to achieve this.
Example 2:

Input: s1 = "delete", s2 = "leet"
Output: 403
Explanation: Deleting "dee" from "delete" to turn the string into "let",
adds 100[d] + 101[e] + 101[e] to the sum.
Deleting "e" from "leet" adds 101[e] to the sum.
At the end, both strings are equal to "let", and the answer is 100+101+101+101 = 403.
If instead we turned both strings into "lee" or "eet", we would get answers of 433 or 417, which are higher.
 

Constraints:

1 <= s1.length, s2.length <= 1000
s1 and s2 consist of lowercase English letters.
'''

class Solution:
    def minimumDeleteSum_why(self, s1: str, s2: str) -> int:
        ## dp[i][j] := min sum after deleting from s1[:i] and s2[:j]
        ## MAKE two strings equal!! NOT two strings sum equal!! f!!
            
        
        N1, N2 = len(s1), len(s2)
        s1=[ord(ss) for ss in s1]
        s2=[ord(ss) for ss in s2]
        
        
        dp = [[float('inf')]*(N2+1) for _ in range(N1+1)]
        
        
        for i in range(1,N1+1):
            dp[i][0] = dp[i-1][0] + s1[i-1]

        for i in range(1,N2+1):
            dp[0][i] = dp[0][i] + s2[i-1]
        dp[0][0] = 0
            
        for i1 in range(1,N1+1):
            for i2 in range(1,N2+1):
                if s1[i1-1] == s2[i2-1]:
                    dp[i1][i2] = dp[i1-1][i2-1]
                else:
                    dp[i1][i2] = min(s1[i1-1]  + dp[i1-1][i2],
                                     s2[i2-1] + dp[i1][i2-1])
                    
        print(dp)
        return dp[-1][-1]
    
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        ## dp[i][j] := min sum after deleting from s1[i:] and s2[:]j
        ## MAKE two strings equal!! NOT two strings sum equal!! f!!
            
        
        N1, N2 = len(s1), len(s2)
        s1=[ord(ss) for ss in s1]
        s2=[ord(ss) for ss in s2]
        
        
        dp = [[float('inf')]*(N2+1) for _ in range(N1+1)]
        
        dp[-1][-1] = 0
        for i in range(N1-1,-1,-1):
            dp[i][-1] = dp[i+1][-1] + s1[i]
        for i in range(N2-1,-1,-1):
            dp[-1][i] = dp[-1][i+1] + s2[i]
        for i in range(N1-1,-1,-1):
            for j in range(N2-1,-1,-1):
                if s1[i] == s2[j]:
                    dp[i][j] = min(dp[i+1][j+1], dp[i][j])
                else:
                    dp[i][j] = min(dp[i+1][j]+s1[i],dp[i][j+1]+s2[j], dp[i][j])
        return dp[0][0]