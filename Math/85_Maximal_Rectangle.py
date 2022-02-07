'''
85. Maximal Rectangle
Hard

6105

103

Add to List

Share
Given a rows x cols binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.

 

Example 1:


Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
Output: 6
Explanation: The maximal rectangle is shown in the above picture.
Example 2:

Input: matrix = [["0"]]
Output: 0
Example 3:

Input: matrix = [["1"]]
Output: 1
 

Constraints:

rows == matrix.length
cols == matrix[i].length
1 <= row, cols <= 200
matrix[i][j] is '0' or '1'.

'''
class Solution:
    def maximalRectangle_2d(self, matrix: List[List[str]]) -> int:

        
        m, n = len(matrix), len(matrix[0])
        

        ## height[i][j] := num of consec 1's above (including) (i,j)
        height = [[0]*(n+1) for _ in range(m+1)]
        
        ## given height[i][j]
        ## left[i][j] record the left most column number l, where at row i, the height between [l, j] are all >= height[i][j]
        ## then we shoudl have a right[i][j] record the right most column number r, where at row i, where the height between [j, r] are all >= height[i][j]
        
        left = [[0]*(n+1) for _ in range(m+1)]
        right = [[float('inf') ]*(n+1) for _ in range(m+1)]
        res = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == "0":
                    continue
                height[i][j] = height[i-1][j] + 1 ## num of consec 1's above (including) (i,j)
                
                ## find the left most index l, there height[i][lj] >= height[i][j] for all lj in [l...j]
                l = j
                for l in range(j,-1,-1):
                    if height[i][l]<height[i][j]:  
                        l += 1
                        break
                left[i][j] = l
                
            for j in range(n-1,-1,-1): ## find right most elt for each (i,j), and then update res
                if height[i][j] == 0:
                    continue         
                r = j
                for r in range(j, n):
                    if height[i][r]<height[i][j]:
                        r -= 1
                        break

                res = max(res, height[i][j] * (r - left[i][j] + 1))
                
        return res
    
    def maximalRectangle_1d(self, matrix: List[List[str]]) -> int:

        
        m, n = len(matrix), len(matrix[0])
        

        ## height[i][j] := num of consec 1's above (including) (i,j)
        height = [0]*(n+1)
        
        ## given height[i][j]
        ## left[i][j] record the left most column number l, where at row i, the height between [l, j] are all >= height[i][j]
        ## then we shoudl have a right[i][j] record the right most column number r, where at row i, where the height between [j, r] are all >= height[i][j]
        
        left =[0]*(n+1)

        res = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == "0":
                    height[j] = 0
                    continue
                height[j] += 1 ## num of consec 1's above (including) (i,j)
                
                ## find the left most index l, there height[i][lj] >= height[i][j] for all lj in [l...j]
                l = j
                for l in range(j,-1,-1):
                    if height[l]<height[j]:  
                        l += 1
                        break
                left[j] = l
                
            for j in range(n-1,-1,-1): ## find right most elt for each (i,j), and then update res
                if height[j] == 0:
                    continue         
                r = j
                for r in range(j, n):
                    if height[r]<height[j]:
                        r -= 1
                        break

                res = max(res, height[j] * (r - left[j] + 1))
                
        return res
    
    def maximalRectangle_2d_left_right_reduced(self, matrix: List[List[str]]) -> int:

        
        m, n = len(matrix), len(matrix[0])
        

        ## height[i][j] := num of consec 1's above (including) (i,j)
        height = [[0]*(n+1) for _ in range(m+1)]
        
        ## given height[i][j]
        ## left[i][j] record the left most column number l, where at row i, the height between [l, j] are all >= height[i][j]
        ## then we shoudl have a right[i][j] record the right most column number r, where at row i, where the height between [j, r] are all >= height[i][j]
        
        left = [[-float('inf')]*(n+1) for _ in range(m+1)] ## for later we take max right
        right = [[float('inf')]*(n+1) for _ in range(m+1)] ## for later we take min right
        res = 0
        for i in range(m):
            lB, rB = 0, n-1 ## left most bound, right most bound
            for j in range(n):
                if matrix[i][j] == "0":
                    lB = j+1 ## i.e. all later heights are all > height at i,j
                    left[i][j] = 0
                    continue
                height[i][j] = height[i-1][j] + 1 ## num of consec 1's above (including) (i,j)
                
                ## find the left most index l, there height[i][lj] >= height[i][j] for all lj in [l...j]
                ## NOTE: if on i-1th row we have height[i-1][lj] >= height[i-1][j] for all lj in [l...j]; 
                ## then it must be true for ith row if mat[i][j], unless there is a zero on the ith row, which is captured by lB
                l = max(left[i-1][j],lB)
                left[i][j] = l
                
            for j in range(n-1,-1,-1): ## find right most elt for each (i,j), and then update res
                # print("rB: ",rB)
                if matrix[i][j] == "0":
                    rB = j-1
                    right[i][j] = n-1
                else:         
                    # print( "i,j",i,j, right[i-1][j])
                    r = min(right[i-1][j],rB)
                    right[i][j] = r
                res = max(res, height[i][j] * (right[i][j] - left[i][j] + 1))
            # print(left[i])
            # print(right[i])
        return res


    # def maximalRectangle_2d_left_right_reduced(self, matrix: List[List[str]]) -> int:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:

        
        m, n = len(matrix), len(matrix[0])
        

        ## height[i][j] := num of consec 1's above (including) (i,j)
        height = [0]*(n+1)
        
        ## given height[i][j]
        ## left[i][j] record the left most column number l, where at row i, the height between [l, j] are all >= height[i][j]
        ## then we shoudl have a right[i][j] record the right most column number r, where at row i, where the height between [j, r] are all >= height[i][j]
        
        left =  [-float('inf')]*(n+1) ## for later we take max right
        right = [float('inf')]*(n+1)  ## for later we take min right
        res = 0
        for i in range(m):
            lB, rB = 0, n-1 ## left most bound, right most bound
            for j in range(n):
                if matrix[i][j] == "0":
                    lB = j+1 ## i.e. all later heights are all > height at i,j
                    left[j] = 0
                    height[j] = 0
                    continue
                height[j] = height[j] + 1 ## num of consec 1's above (including) (i,j)
                
                ## find the left most index l, there height[i][lj] >= height[i][j] for all lj in [l...j]
                ## NOTE: if on i-1th row we have height[i-1][lj] >= height[i-1][j] for all lj in [l...j]; 
                ## then it must be true for ith row if mat[i][j], unless there is a zero on the ith row, which is captured by lB
                l = max(left[j],lB)
                left[j] = l
                
            for j in range(n-1,-1,-1): ## find right most elt for each (i,j), and then update res
                # print("rB: ",rB)
                if matrix[i][j] == "0":
                    rB = j-1
                    right[j] = n-1
                else:         
                    # print( "i,j",i,j, right[i-1][j])
                    r = min(right[j],rB)
                    right[j] = r
                res = max(res, height[j] * (right[j] - left[j] + 1))
            # print(left[i])
            # print(right[i])
        return res

    
        
