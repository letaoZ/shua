'''
340. Longest Substring with At Most K Distinct Characters
Medium

2076

65

Add to List

Share
Given a string s and an integer k, return the length of the longest substring of s that contains at most k distinct characters.

 

Example 1:

Input: s = "eceba", k = 2
Output: 3
Explanation: The substring is "ece" with length 3.
Example 2:

Input: s = "aa", k = 1
Output: 2
Explanation: The substring is "aa" with length 2.
 

Constraints:

1 <= s.length <= 5 * 104
0 <= k <= 50
'''

class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        if k == 0:
            return 0
        
        cnt = dict()
        left_end = 0
        cur_k = 0
        res = 0
        for i in range(len(s)):
            cnt[s[i]] = cnt.get(s[i],0) + 1
            if len(cnt)<=k:
                pass
            else:
                while cnt[s[left_end]] >0:
                    cnt[s[left_end] ] -= 1
                    if cnt[s[left_end]] == 0:
                        del cnt[s[left_end]]
                        left_end += 1
                        break
                    left_end += 1
                    
            res = max(res, i-left_end+1)
            
        return res
                    