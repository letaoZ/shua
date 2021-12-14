
'''
139. Word Break
Medium

8816

403

Add to List

Share
Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.

 

Example 1:

Input: s = "leetcode", wordDict = ["leet","code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
Example 2:

Input: s = "applepenapple", wordDict = ["apple","pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
Note that you are allowed to reuse a dictionary word.
Example 3:

Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: false
 

Constraints:

1 <= s.length <= 300
1 <= wordDict.length <= 1000
1 <= wordDict[i].length <= 20
s and wordDict[i] consist of only lowercase English letters.
All the strings of wordDict are unique.'''

class Solution:
    def wordBreak_slow(self, s: str, wordDict: List[str]) -> bool:
        if not wordDict:
            return len(s) == 0
        
        
        wordDict = list(set(wordDict))
        
        
        ## dp[i][j]: string[i:j] can be represented
        
        N = len(s)
        dp = [ [0]*(N+1) for _ in range(N)]
        for i in range(N):
            dp[i][i] = 1
        
        ## dp[i][j] = (dp[i][k] and dp[k][j])
        ## need to make this faster
        MIN_LEN= min([len(_) for _ in wordDict])
        
        def searching(s,dp,i,j):
            if i>= j or dp[i][j]:
                return True
            
            if j-i<MIN_LEN:
                return False
            
            if s[i:j] in wordDict:
                dp[i][j] = True
                return True
            
            for k in range(i+MIN_LEN,j):
                dp[i][j] = (searching(s,dp,i,k) and searching(s, dp,k,j))
                if dp[i][j]:
                    return True
                
            return False
        
        res = searching(s,dp,0,N)
        return res
    
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if not wordDict:
            return len(s) == 0
        
        
        wordDict = list(set(wordDict))
        MAX_LEN = max(len(s), max([len(_) for _ in wordDict]))
        
        ## dp[j]: string[:j] can be represented
        ## dp[j] = dp[i] and word[i:j] in wordDict for some i
        N = len(s)
        dp = [0]*(N+1)
        dp[0] = 1
        
        for j in range(1,N+1):
            res = False
            for i in range(max(0, j-MAX_LEN), j):
                res = (dp[i] and s[i:j] in wordDict)
                if res:
                    break
            dp[j] = res
        return dp[-1]
                
                
        
        
        