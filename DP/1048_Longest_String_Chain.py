'''
1048. Longest String Chain
Medium

2867

139

Add to List

Share
You are given an array of words where each word consists of lowercase English letters.

wordA is a predecessor of wordB if and only if we can insert exactly one letter anywhere in wordA without changing the order of the other characters to make it equal to wordB.

For example, "abc" is a predecessor of "abac", while "cba" is not a predecessor of "bcad".
A word chain is a sequence of words [word1, word2, ..., wordk] with k >= 1, where word1 is a predecessor of word2, word2 is a predecessor of word3, and so on. A single word is trivially a word chain with k == 1.

Return the length of the longest possible word chain with words chosen from the given list of words.

 

Example 1:

Input: words = ["a","b","ba","bca","bda","bdca"]
Output: 4
Explanation: One of the longest word chains is ["a","ba","bda","bdca"].
Example 2:

Input: words = ["xbc","pcxbcf","xb","cxbc","pcxbc"]
Output: 5
Explanation: All the words can be put in a word chain ["xb", "xbc", "cxbc", "pcxbc", "pcxbcf"].
Example 3:

Input: words = ["abcd","dbqca"]
Output: 1
Explanation: The trivial word chain ["abcd"] is one of the longest word chains.
["abcd","dbqca"] is not a valid word chain because the ordering of the letters is changed.
 

Constraints:

1 <= words.length <= 1000
1 <= words[i].length <= 16
words[i] only consists of lowercase English letters.
'''



class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        ## NOTE: you can only go from length: L to L+1
        words_dict = collections.defaultdict(list)
        max_l = 0
        for w in words:
            l = len(w)
            words_dict[l].append(w)
            max_l = max(l,max_l)
        
        if len(words_dict)<=1:
            return len(words_dict)
        res = 1
        word_path_length = {w:1 for w in words} ## longest path ending with w
        ## assume K distinct length
        ## at most len(words)
        # for each length l:
        #   for each word of length l, we check all its letters: time: O(len(w))
        # so for each length l: time complexity = O(sum(len(w_l)))
        ## so complexity = O(sum(len(w)))
        for l in range(1,max_l + 1):
            if l-1 not in words_dict:
                continue
            for w in words_dict[l]:
                for missing_i in range(len(w)):
                    wt = w[:missing_i] + w[missing_i+1:]
                    if wt in words_dict[l-1]:
                        word_path_length[w] = max(word_path_length[wt]+1,word_path_length[w])
                        res = max(word_path_length[w],res)
        return res    
                
            