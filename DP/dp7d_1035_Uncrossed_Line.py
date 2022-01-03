'''
1035. Uncrossed Lines
Medium

1485

24

Add to List

Share
You are given two integer arrays nums1 and nums2. We write the integers of nums1 and nums2 (in the order they are given) on two separate horizontal lines.

We may draw connecting lines: a straight line connecting two numbers nums1[i] and nums2[j] such that:

nums1[i] == nums2[j], and
the line we draw does not intersect any other connecting (non-horizontal) line.
Note that a connecting line cannot intersect even at the endpoints (i.e., each number can only belong to one connecting line).

Return the maximum number of connecting lines we can draw in this way.

 

Example 1:


Input: nums1 = [1,4,2], nums2 = [1,2,4]
Output: 2
Explanation: We can draw 2 uncrossed lines as in the diagram.
We cannot draw 3 uncrossed lines, because the line from nums1[1] = 4 to nums2[2] = 4 will intersect the line from nums1[2]=2 to nums2[1]=2.
Example 2:

Input: nums1 = [2,5,1,2,5], nums2 = [10,5,2,1,5,2]
Output: 3
Example 3:

Input: nums1 = [1,3,7,1,7,5], nums2 = [1,9,2,5,1]
Output: 2
'''
class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        ## each number can only belong to one connecting line!!
        m, n = len(nums1), len(nums2)
        
        ## dp[i][j] max overlapping nums you get 
        dp = [ [0]*(n+1) for _ in range(m+1) ] 
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                if nums1[i] == nums2[j]: ## first come first serve the line. each end point only used once. so we take the farthest possible
                    dp[i][j] = dp[i+1][j+1] + 1
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j+1]) ## note: j+1 is visited before j
                    
        return dp[0][0]
        