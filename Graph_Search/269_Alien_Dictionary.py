'''
269. Alien Dictionary
Hard

3298

678

Add to List

Share
There is a new alien language that uses the English alphabet. However, the order among the letters is unknown to you.

You are given a list of strings words from the alien language's dictionary, where the strings in words are sorted lexicographically by the rules of this new language.

Return a string of the unique letters in the new alien language sorted in lexicographically increasing order by the new language's rules. If there is no solution, return "". If there are multiple solutions, return any of them.

A string s is lexicographically smaller than a string t if at the first letter where they differ, the letter in s comes before the letter in t in the alien language. If the first min(s.length, t.length) letters are the same, then s is smaller if and only if s.length < t.length.

 

Example 1:

Input: words = ["wrt","wrf","er","ett","rftt"]
Output: "wertf"
Example 2:

Input: words = ["z","x"]
Output: "zx"
Example 3:

Input: words = ["z","x","z"]
Output: ""
Explanation: The order is invalid, so return "".
 

Constraints:

1 <= words.length <= 100
1 <= words[i].length <= 100
words[i] consists of only lowercase English letters.
'''

class Solution:
    def alienOrder(self, words: List[str]) -> str:
        ## num of vertices = letters = 26
        ## nums of edges = len(words)
        ## time complexity = O(len(words) + letters)
        ## g[a] indicates a < g[a]
        g = collections.defaultdict(set)
        
        
        ## build g
        def searching(i,words,g): ## from words[i] to words[i+1]
            if i == len(words) - 1:
                return True
            
            
            frm = words[i]
            to = words[i+1]
            l = min(len(frm), len(to))
            for j in range(l):
                if frm[j] == to[j]:
                    continue
                g[frm[j]].add(to[j])
                return True
            if len(frm) > len(to):
                return False
            else:
                return True
        


        for i in range(len(words)-1):
            if not searching(i,words,g):
                  return "" 

            
        
        ## top. sort find cycles
        ## visited[i] == 1, visiting, 2, finished visiting, 0 haven't visited
        ## first we need to mark what letters are available
        visited = collections.defaultdict(int) 
                      
        for w in words:
            for ss in set(w):
                visited[ss] = 0
                      
            
        res = []
        def dfs(letter, visited, res, g):
            
            if visited[letter] == 1:
                return False
            if visited[letter] == 2:
                return True
            visited[letter] = 1
            for w in g[letter]:
                if not dfs(w,visited,res,g):
                    return False
            res.append(letter)
            visited[letter] = 2
            return True

        for v in visited:
            if visited[v] == 2:
                continue
                
            if not dfs(v, visited, res, g):
                return ""
        return "".join(res[::-1])
        