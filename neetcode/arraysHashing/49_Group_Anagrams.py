'''
49. Group Anagrams
Medium

10700

344

Add to List

Share
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:

Input: strs = [""]
Output: [[""]]
Example 3:

Input: strs = ["a"]
Output: [["a"]]
 

Constraints:

1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.
'''
from typing import *
import collections
def getAna(candi,trace, res):

    if len(candi) == 0:
        res.add("".join(trace))
        return
    
    for i,l in enumerate(candi):
        if i>0 and candi[i] == candi[i-1]:
            continue
        getAna(candi[:i] + candi[i+1:],trace + [l], res)

def generateAna(ss):
    ## return all anagram of ss
    res = set()
    getAna(ss,[],res)
    return res

    

class Solution:
    
    def groupAnagrams_sort(self, strs: List[str]) -> List[List[str]]:
        res_dict = collections.defaultdict(list)
        for ss in strs:
            ss_sorted = [_ for _ in ss]
            ss_sorted.sort()
            res_dict[''.join(ss_sorted) ].append(ss)
            
        res = list(res_dict.values())
        return res
        
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ## since we know 26 letters -- these come with  a natural order
        ## We can record ALL letters in order and build a tag (without using sort)
        ## However, actual run time still slow as we use "counter" 
        ans = collections.defaultdict(list)
        letters = [chr(i + ord('a')) for i in range(26)]
        for ss in strs:
            ss_cnt = collections.Counter(ss)
            tag = "".join([l*ss_cnt[l] for l in letters if l in ss_cnt])
            # print(ss, tag)
            ans[tag].append(ss)
            
        res = [ll for _,ll in ans.items()]
        return res
    