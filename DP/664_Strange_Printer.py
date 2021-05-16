'''
664. Strange Printer
Hard
There is a strange printer with the following two special properties:

The printer can only print a sequence of the same character each time.
At each turn, the printer can print new characters starting from and ending at any place and will cover the original existing characters.
Given a string s, return the minimum number of turns the printer needed to print it.


Example 1:

Input: s = "aaabbb"
Output: 2
Explanation: Print "aaa" first and then print "bbb".
Example 2:

Input: s = "aba"
Output: 2
Explanation: Print "aaa" first and then print "b" from the second place of the string, which will cover the existing character 'a'.
 

Constraints:

1 <= s.length <= 100
s consists of lowercase English letters.
'''

import re
class Solution(object):
    
    
    def strangePrinter_topdown(self, s):
        '''
        The problem wants us to find the number of ways to do something without giving specific steps like how to achieve it. This can be a typical signal that dynamic programming may come to help.

        dp[i][j] stands for the minimal turns we need for string from index i to index j.
        So we have

        dp[i][i] = 1: we need 1 turn to paint a single character.
        dp[i][i + 1]
        dp[i][i + 1] = 1 if s.chartAt(i) == s.charAt(i + 1)
        dp[i][i + 1] = 2 if s.chartAt(i) != s.charAt(i + 1)
        Then we can iteration len from 2 to possibly n. For each iteration, we iteration start index from 0 to the farthest possible.

        The maximum turns for dp[start][start + len] is len + 1, i.e. print one character each time.
        We can further divide the substring to two parts: start -> start+k and start+k+1 -> start+len. It is something as following:
        index |start  ...  start + k| |start + k + 1 ... start + len|
        char  |  a    ...       b   | |      c       ...      b     |
        As shown above, if we have s.charAt(start + k) == s.charAt(start + len), we can make it in one turn when we print this character (i.e. b here)
        This case we can reduce our turns to dp[start][start + k] + dp[start + k + 1][start + len] - 1

        
        '''

        ## regx
        s = re.sub(r'(.)\1+', r'\1', s)
        
        ## 
        ## dp[i][j]: number of ways to cover s[i:j+1]
        ## dp[i][i] = 1, dp[i][i+1] = 2 if s[i]!=s[i+1] else 2
        ##
                
        sz = len(s)
        dp = [[sz]*(sz+1) for _ in range(sz + 1)]
        for i in range(sz-1):
            dp[i][i] = 1
            
        
        ## length is 3
        for ll in range(2, sz+1):
            for i in range(sz-ll+1):
                j = i + ll - 1
                ## just paint the last one anyways
                dp[i][j] = dp[i][j-1] + 1
                for k in range(i,j+1):
                    if s[j] == s[k]:
                        dp[i][j] = min(dp[i][j], dp[i][k] + dp[k+1][j] - 1)
        return dp[0][sz-1]
        
   
    
    def strangePrinter_bottomUP(self, s):
        cache = {'':0}

        def solve(s):

            if s in cache:
                return cache[s]
            # cost to simply insert last character
            cost = solve(s[0:-1]) + 1
            # what if last character could be inserted for free just by reusing previous step that already prints it?
            # eg. I have AbcAdeA
            # whatever steps I used to print the first part: AbcA| ,  
            # will have to cover the last A of the first part, if it covers the
            # last A of the first part, then it automatically extends to cover AbcA|...A
			# . . . . . A . . . . A
			# |---------| |-----| last character is free
            char_to_insert = s[-1]
            for i, c in enumerate(s[:-1]):
                if c == char_to_insert:
                    cost = min(cost, solve(s[0:i + 1]) + solve(s[i + 1:-1]))
            cache[s] = cost
            return cost
        ## solution remains the same if you remove all duplicates
        
        s = re.sub(r'(.)\1+',r'\1',s)
        return solve(s)
    
    def strangePrinter_noRegex(self, s):
        cache = {'':0}

        def solve(s):
            
            if s in cache:
                return cache[s]
            # cost to simply insert last character
            cost = solve(s[0:-1]) + 1
            # what if last character could be inserted for free just by reusing previous step that already prints it?
			# . . . . . A . . . . A
			# |---------| |-----| last character is free
            char_to_insert = s[-1]
            for i, c in enumerate(s[:-1]):
                if c == char_to_insert:
                    cost = min(cost, solve(s[0:i + 1]) + solve(s[i + 1:-1]))
            cache[s] = cost
            return cost
        ## solution remains the same if you remove all duplicates
        
        s = list(s)
        l = 0
        for i in range(len(s)):
            if s[i] == s[l]:
                continue
            l += 1
            s[l] = s[i]
        s = ''.join(s[:l+1])
        
        print(tt)
        return solve(s)