'''
28. Implement strStr()
Easy

3655

3423

Add to List

Share
Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Clarification:

What should we return when needle is an empty string? This is a great question to ask during an interview.

For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().

 

Example 1:

Input: haystack = "hello", needle = "ll"
Output: 2
Example 2:

Input: haystack = "aaaaa", needle = "bba"
Output: -1
Example 3:

Input: haystack = "", needle = ""
Output: 0
 

Constraints:

0 <= haystack.length, needle.length <= 5 * 104
haystack and needle consist of only lower-case English characters.
'''class Solution:
    
    def get_int(self,ss):
        return ord(ss) - ord('a')
        
    def build_auto(self,pat):
        ## given a pattern, build its finite automata
        ## eg. pat = "ababc" state transformatoin: 0 (a) 1 (b) 2 (a) 3 (b) 4 (c) 5
        ## start from the beginning till letter i of the pattern: dp[i][c] := at state (i) using letter c, the farthest we can map to with in pat
        ## dp[0]['a'] = 1
        ## since we have 26 letters, 'a'->0 etc
        
        dp = [ [0]*26 for _ in range(len(pat)) ]
        dp[0][self.get_int(pat[0])] = 1
        
        shadow_x = 0
        for i in range(1,len(pat)):
            my_c = self.get_int(pat[i]) ## pat[i]'s next state is i+1
            for c in range(26):
                if c == my_c: ## go to next stage
                    dp[i][c] = i+1
                else:
                    dp[i][c] = dp[shadow_x][c] ## previous stage with same prefix pattern furthest it reaches
            shadow_x = dp[shadow_x][my_c]
            
        return dp
        
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) == 0:
            return 0
        if len(haystack) == 0:
            return -1
        
        
        dp = self.build_auto(needle)
        
        next_state = 0
        for i,h in enumerate(haystack):
            my_c = self.get_int(h)
            next_state = dp[next_state][my_c]
            if next_state == len(needle):
                return i - len(needle) + 1
            
        return -1
            