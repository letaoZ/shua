'''
424. Longest Repeating Character Replacement
Medium

5552

217

Add to List

Share
You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.

 

Example 1:

Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.
Example 2:

Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
 

Constraints:

1 <= s.length <= 105
s consists of only uppercase English letters.
0 <= k <= s.length

'''
import collections
from typing import *
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ## idea: for each window s[l...r], keep the letter repeats the most of times, and replace the rest by that letter
        
        l = 0
        
        cnt = collections.defaultdict(int)
        max_repeat = 0 
        res = 0
        for r in range(len(s)):
            cnt[s[r]] += 1
            max_repeat = max(cnt[s[r]], max_repeat)
            ##means current window needs to replace more than k letters
            if r - l + 1 - max_repeat > k: 
                cnt[s[l]] -= 1
                l += 1
            
            res = max(res, r - l + 1)
        return res