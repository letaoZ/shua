'''
159. Longest Substring with At Most Two Distinct Characters
Medium

1560

26

Add to List

Share
Given a string s, return the length of the longest substring that contains at most two distinct characters.

 

Example 1:

Input: s = "eceba"
Output: 3
Explanation: The substring is "ece" which its length is 3.
Example 2:

Input: s = "ccaabbb"
Output: 5
Explanation: The substring is "aabbb" which its length is 5.
 

Constraints:

1 <= s.length <= 105
s consists of English letters.
'''

class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        res = 1
        left_end = 0
        letters = [None, [s[0],0] ]
        for i in range(1,len(s)):
            if s[i] == letters[1][0]:
                pass
            else:
                if letters[0] is None:
                    letters[0] = letters[1]
                    letters[1] = [s[i],i]
                elif letters[0][0] == s[i]:
                    letters[0], letters[1] = letters[1], [s[i],i]
                else:
                    left_end = letters[1][1]
                    letters[0], letters[1] = letters[1], [s[i],i]
                    

            # print(letters)
            res = max(res, i-left_end + 1)
            # print(res)
            # print("left_endL: ", left_end)
            

        return res
        
    def lengthOfLongestSubstringTwoDistinct_generalize_to_k(self, s: str) -> int:
        cnt = dict()
        left_end = 0
        k = 2
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