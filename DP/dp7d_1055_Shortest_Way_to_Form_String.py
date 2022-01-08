'''
1055. Shortest Way to Form String
Medium

775

46

Add to List

Share
A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

Given two strings source and target, return the minimum number of subsequences of source such that their concatenation equals target. If the task is impossible, return -1.

 

Example 1:

Input: source = "abc", target = "abcbc"
Output: 2
Explanation: The target "abcbc" can be formed by "abc" and "bc", which are subsequences of source "abc".
Example 2:

Input: source = "abc", target = "acdbc"
Output: -1
Explanation: The target string cannot be constructed from the subsequences of source string due to the character "d" in target string.
Example 3:

Input: source = "xyz", target = "xzyxz"
Output: 3
Explanation: The target string can be constructed as follows "xz" + "y" + "xz".
 

Constraints:

1 <= source.length, target.length <= 1000
source and target consist of lowercase English letters.
'''

class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        
        for tt in target:
            if tt not in source:
                return -1
            
        ## keep track of each letters' earliest index 
        source_dict = dict()
        for ii, ss in enumerate(source):
            source_dict[ss]=min(source_dict.get(ss,ii), ii)
        
        
        i = 0
        cnt = 0
        source_idx = len(source)
        ## for each letter in target we try to match the longest source possible
        while i < len(target):
            source_idx = source_dict[target[i]]
            while source_idx < len(source) and i<len(target):
                if target[i] == source[source_idx]:
                    i += 1
                source_idx += 1

            cnt += 1
            
        return cnt