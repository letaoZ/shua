'''
1039. Minimum Score Triangulation of Polygon
Medium


You have a convex n-sided polygon where each vertex has an integer value. You are given an integer array values where values[i] is the value of the ith vertex (i.e., clockwise order).

You will triangulate the polygon into n - 2 triangles. For each triangle, the value of that triangle is the product of the values of its vertices, and the total score of the triangulation is the sum of these values over all n - 2 triangles in the triangulation.

Return the smallest possible total score that you can achieve with some triangulation of the polygon.

Example 1:

Input: values = [1,2,3]
Output: 6
Explanation: The polygon is already triangulated, and the score of the only triangle is 6.
Example 2:


Input: values = [3,7,4,5]
Output: 144
Explanation: There are two triangulations, with possible scores: 3*7*5 + 4*5*7 = 245, or 3*4*5 + 3*4*7 = 144.
The minimum score is 144.
Example 3:


Input: values = [1,3,1,4,1,5]
Output: 13
Explanation: The minimum score triangulation has score 1*1*3 + 1*1*4 + 1*1*5 + 1*1*1 = 13.
 

Constraints:

n == values.length
3 <= n <= 50
1 <= values[i] <= 100
'''

class Solution: 
    def minScoreTriangulation_dp_2d_bottomup(self, nums: List[int]) -> int:
        sz = len(nums)
        
        dp = [ [0]*(sz) for _ in range(sz)]
    
        for L in range(2,sz):
            for i in range(sz-L):
                j = i+L
                dp[i][j] = float(('inf'))
                for k in range(i+1,j):
                    dp[i][j] = min(
                        dp[i][j], 
                        dp[i][k] + dp[k][j]+nums[i]*nums[j]*nums[k])

        return dp[0][sz-1]

    def minScoreTriangulation_topdown(self, nums: List[int]) -> int:
        dp = {}
        
        def searching(nums,i,j):
            if (i,j) in dp:
                return dp[(i,j)]
            
            res = float('inf')
            if i+1 >= j:
                res = 0
            else:
                for k in range(i+1,j):
                    res = min(res, nums[i]*nums[j]*nums[k]+searching(nums,i,k) + searching(nums,k,j))
            dp[(i,j)] = res
            return res
        
        searching(nums, 0, len(nums)-1)

        return dp[(0, len(nums)-1)]
    def minScoreTriangulation_slow(self, values: List[int]) -> int:
        
        dp = {}   
        ## shift of tag == shift tagr?
        
        def checking(tag,val, dp):
            tag = tag.split('_')
            for i in range(len(tag)):
                tagr = '_'.join(tag[i:] + tag[:i])
                dp[tagr] = val
            
            
        def searching(nums):
            tag = '_'.join([str(n) for n in nums])
            if len(nums) <= 2:
                return 0
            if tag in dp:
                return dp[tag]
            if len(nums) == 3:
                p = 1
                for v in nums:
                    p *= v
                checking(tag,p, dp)
                return p
            
            p0 = nums[0]*nums[1]
            res = float('inf')
            for k in range(2,len(nums)):
                p = p0*nums[k]
                res = min(res, 
                          p + searching(nums[1:k+1]) + searching(nums[k:]+nums[:1]))
            checking(tag,res, dp)
            return res
        
        res = searching(values)
        return res