'''
1901. Find a Peak Element II
Medium

517

39

Add to List

Share
A peak element in a 2D grid is an element that is strictly greater than all of its adjacent neighbors to the left, right, top, and bottom.

Given a 0-indexed m x n matrix mat where no two adjacent cells are equal, find any peak element mat[i][j] and return the length 2 array [i,j].

You may assume that the entire matrix is surrounded by an outer perimeter with the value -1 in each cell.

You must write an algorithm that runs in O(m log(n)) or O(n log(m)) time.

 

Example 1:



Input: mat = [[1,4],[3,2]]
Output: [0,1]
Explanation: Both 3 and 4 are peak elements so [1,0] and [0,1] are both acceptable answers.
Example 2:



Input: mat = [[10,20,15],[21,30,14],[7,16,32]]
Output: [1,1]
Explanation: Both 30 and 32 are peak elements so [1,1] and [2,2] are both acceptable answers.
 

Constraints:

m == mat.length
n == mat[i].length
1 <= m, n <= 500
1 <= mat[i][j] <= 105
No two adjacent cells are equal.
'''



class Solution:
    def findPeakGrid_slow(self, mat):
        
        visited = set()
        m, n =len(mat), len(mat[0])
        res = []
        for i in range(m):
            for j in range(n):
                if (i,j) in visited:
                    continue
                v = mat[i][j]
                if i+1<m:
                    if mat[i+1][j]>=v:
                        continue
                if i - 1>=0:
                    if mat[i-1][j] >= v:
                        continue
                if j+1<n:
                    if mat[i][j+1]>=v:
                        continue
                if j-1>=0:
                    if mat[i][j-1] >=v:
                        continue
                return [i,j]
        return []
    def findPeakGrid(self, mat):
        startCol = 0
        endCol = len(mat[0])-1
       
        while startCol <= endCol:
            maxRow = 0
            midCol = startCol + (endCol - startCol)//2
            
            for row in range(len(mat)):
                maxRow = row if (mat[row][midCol] >= mat[maxRow][midCol]) else maxRow
            
            leftIsBig    =   midCol-1 >= startCol  and  mat[maxRow][midCol-1] > mat[maxRow][midCol]
            rightIsBig   =   midCol+1 <= endCol    and  mat[maxRow][midCol+1] > mat[maxRow][midCol]
            
            if (not leftIsBig) and (not rightIsBig): #we have found the peak element
                return [maxRow, midCol]
            elif rightIsBig:
                #if rightIsBig, then there is an element in 'right' 
                # that is bigger than all the elements in the 'midCol', 
                startCol = midCol+1     
                # so 'midCol' cannot have 'peakPlane'
            else:                           
                # leftIsBig
                endCol = midCol-1
                
        return [-1,-1]