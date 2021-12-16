
'''
119. Pascal's Triangle II
Easy

2025

248

Add to List

Share
Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:


 

Example 1:

Input: rowIndex = 3
Output: [1,3,3,1]
Example 2:

Input: rowIndex = 0
Output: [1]
Example 3:

Input: rowIndex = 1
Output: [1,1]
 

Constraints:

0 <= rowIndex <= 33
'''

class Solution:
    def getRow_2d(self, rowIndex: int) -> List[int]:

        
        if rowIndex < 0:
            return [[]]
        numRows = rowIndex+1
        dp = [[1]*(1+i) for i in range(numRows)]
        
        for k in range(2,numRows):
            for ik in range(1,k):
                dp[k][ik] = dp[k-1][ik-1] + dp[k-1][ik]
                
        return dp[rowIndex]
    
    def getRow(self, rowIndex: int) -> List[int]:

        ## reduce to 1d
        if rowIndex < 0:
            return [[]]
        numRows = rowIndex+1
        dp = [1]*numRows
        
        ## reduce dimension
        for k in range(1,numRows):
            for ik in range(k-1,0,-1):
                dp[ik] = dp[ik-1] + dp[ik]
                
        return dp