'''
76. Minimum Window Substring
Hard

8935

507

Add to List

Share
Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

A substring is a contiguous sequence of characters within the string.

 

Example 1:

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
Example 2:

Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.
Example 3:

Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.
 

Constraints:

m == s.length
n == t.length
1 <= m, n <= 105
s and t consist of uppercase and lowercase English letters.
 

Follow up: Could you find an algorithm that runs in O(m + n) time?
'''

class Solution:
    def minWindow_brutal(self, s: str, t: str) -> str:
        ## slow but works
        
        m,n = len(s), len(t)
        if m<n or n==0:
            return ""
        for tt in t:
            if tt not in s:
                return ""
        ## for every length give it a try
        
        def maxOverLap(a,b):
            dp = [[0]*(len(b)+1) for _ in range(len(a)+1) ]
            res = 0
            for i in range(len(a)-1,-1,-1):
                for j in range(len(b)-1,-1,-1):
                    if a[i] == b[j]:
                        dp[i][j] = dp[i+1][j+1] + 1
                    else:
                        dp[i][j] = max(dp[i][j+1], dp[i+1][j])
                        
                    if dp[i][j] ==len(b) :
                        return len(b)
                    
            return dp[0][0]
        def searching(s_long,s_short):
            s_long_list = [_ for _ in s_long]
            s_short_list = [_ for _ in s_short]
            s_long_list.sort()
            s_short_list.sort()
            res  = maxOverLap(s_long_list, s_short_list)
            return res
        for L in range(n, m+1):
            for i in range(0,m-L+1):
                # print(s[i:i+L])
                res = searching(s[i:i+L], t)
                if res == n:
                    return s[i:i+L]
        return ""
    def minWindow_brutal_with_window(self, s: str, t: str) -> str:
        m,n = len(s), len(t)
        if m<n or n==0:
            return ""
        for tt in t:
            if tt not in s:
                return ""
        ## for every length give it a try
        
        def maxOverLap(a,b):
            dp = [[0]*(len(b)+1) for _ in range(len(a)+1) ]
            res = 0
            for i in range(len(a)-1,-1,-1):
                for j in range(len(b)-1,-1,-1):
                    if a[i] == b[j]:
                        dp[i][j] = dp[i+1][j+1] + 1
                    else:
                        dp[i][j] = max(dp[i][j+1], dp[i+1][j])
                        
                    if dp[i][j] ==len(b) :
                        return len(b)
                    
            return dp[0][0]
        def searching(s_long,s_short):
            s_long_list = [_ for _ in s_long]
            s_short_list = [_ for _ in s_short]
            s_long_list.sort()
            s_short_list.sort()
            res  = maxOverLap(s_long_list, s_short_list)
            return res
        
        ## sliding window
        l = r = 0
        res = float('inf')
        res_s = ""
        for r in range(n,m+1):
            cur_len = searching(s[l:r],t)
            if cur_len==n:
                
                while cur_len == n and r-l>=n:
                    if res >r-l:
                        res = r-l
                        res_s = s[l:r]
                    l += 1
                    cur_len = searching(s[l:r],t)
            
        return res_s
    
    
    def minWindow(self, s: str, t: str) -> str:
        ## two dict
        m,n = len(s), len(t)
        if m<n or n==0:
            return ""
        for tt in t:
            if tt not in s:
                return ""
            
        ## for each letter in t, we can count number of letter needed by t
        ## t = "aabd" : a2, b1, d1
        window = collections.defaultdict(int)
        need = {}
        for tt in t:
            need[tt] = need.get(tt,0)+1
        total = 0
        l, r = 0, 0
        res_len = float('inf')
        res_series = ""
        for r in range(m):
            ss = s[r]
            # print(ss)
            if ss in need:
                window[ss] += 1
                if need[ss]==window[ss]:
                    total += 1
            # print(need)
            # print(total)
            # print()
            while( total == len(need) ):
                sl = s[l]
                if res_len>r-l+1:
                    res_len = r-l+1
                    res_series = s[l:r+1]
                if sl not in need:
                    pass
                elif need[sl] == window[sl]:
                    total -= 1
                    window[s[l]] -= 1
                elif need[sl]<window[sl]:
                    window[sl] -= 1
                l += 1

            print("new_ left: ", l)
            print()
        return res_series