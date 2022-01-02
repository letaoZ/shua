'''
74. Search a 2D Matrix
Medium

5322

235

Add to List

Share
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
 

Example 1:


Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true
Example 2:


Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false
 

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 100
-104 <= matrix[i][j], target <= 104
Accepted

'''


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        m = len(matrix)
        if m == 0:
            return False
        
        n = len(matrix[0])
        if n == 0:
            return False
        
        def get_idx(k,m,n):
            i = k//n
            j = k - i*n
            
            return (i, j)
        
        l, r = 0, (m*n) -1
        
        while l<=r:
            mid = l + (r-l)//2
            
            i,j = get_idx(mid,m,n)
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] < target:
                
                l = mid+1
            elif matrix[i][j] > target:
                r = mid-1
        return False
            