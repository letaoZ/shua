'''
212. Word Search II
Hard

6370

258

Add to List

Share
Given an m x n board of characters and a list of strings words, return all words on the board.

Each word must be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

 

Example 1:


Input: board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","pea","eat","rain"]
Output: ["eat","oath"]
Example 2:


Input: board = [["a","b"],["c","d"]], words = ["abcb"]
Output: []
 

Constraints:

m == board.length
n == board[i].length
1 <= m, n <= 12
board[i][j] is a lowercase English letter.
1 <= words.length <= 3 * 104
1 <= words[i].length <= 10
words[i] consists of lowercase English letters.
All the strings of words are unique.

'''
from collections import defaultdict
from typing import *
class TrieNode():
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.isWord = False

class Trie():
    def __init__(self):
        self.root = TrieNode()
        self.num_of_words = 0
    
    def insert(self, word):
        node = self.root
        for w in word:
            node = node.children[w]
        node.isWord = True
        self.num_of_words += 1

class Solution(object):
    def dfs(self, i, j, trie, node, board, word, res):
        if not node or trie.num_of_words == 0:
            return
        if node.isWord:
            res.append(word)
            node.isWord = False
            trie.num_of_words -= 1

        tmp = board[i][j]
        board[i][j] = '#'
        if i + 1 < len(board):
            c = board[i + 1][j]
            self.dfs(i + 1, j, trie, node.children.get(c), board, word + c, res)
        if j + 1 < len(board[0]):
            c = board[i][j + 1]
            self.dfs(i, j + 1, trie, node.children.get(c), board, word + c, res)
        if i - 1 >= 0:
            c = board[i - 1][j]
            self.dfs(i - 1, j, trie, node.children.get(c), board, word + c, res)
        if j - 1 >= 0:
            c = board[i][j - 1]
            self.dfs(i, j - 1, trie, node.children.get(c), board, word + c, res)
        board[i][j] = tmp

    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        res = []
        trie = Trie()
        node = trie.root
        for w in words:
            trie.insert(w)
        for i in range(len(board)):
            for j in range(len(board[0])):
                self.dfs(i, j, trie, node.children[board[i][j]], board, board[i][j], res)
        return res
    
class Solution_brutal:
    
    
    def findOneWord(self, board, word):
        def dfs(wi,word,i,j,board,visited):
            if wi == len(word):
                res[0] = True
                return True
            if res[0]:
                return True
            for dx, dy in ((0,1),(0,-1),(1,0),(-1,0),):
                x, y = i+ dx, j + dy
                if not ( 0<= x < m and 0<= y<n): continue
                if visited[x][y]: continue
                if word[wi] != board[x][y]: continue
                visited[x][y] = 1
                if dfs(wi+1, word, x,y,board,visited):
                    res[0] = True
                    return True
                visited[x][y] = 0
                
            return False
        
        
        m, n = len(board), len(board[0])
        
        
        
        ans = []
        for i in range(m):
            for j in range(n):
                if word[0]!=board[i][j]:
                    continue
                visited = [ [0]*n for _ in range(m)]
                visited[i][j] = 1
                res = [0]
                dfs(1, word,i,j,board,visited)
                if res[0]:
                    
                    return word
        return None
                    
                
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        ans = []
        
        for word in words:
            res = self.findOneWord(board,word)
            if res: ans.append(res)
                
        return ans