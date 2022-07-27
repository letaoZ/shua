'''
84. Largest Rectangle in Histogram
Hard

11182

157

Add to List

Share
Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, 
return the area of the largest rectangle in the histogram.

 

Example 1:


Input: heights = [2,1,5,6,2,3]
Output: 10
Explanation: The above is a histogram where width of each bar is 1.
The largest rectangle is shown in the red area, which has an area = 10 units.
Example 2:


Input: heights = [2,4]
Output: 4
 

Constraints:

1 <= heights.length <= 105
0 <= heights[i] <= 104

'''

from typing import *
class Solution:

    def largestRectangleArea(self, height: List[int]) -> int:
        height.append(0)
        stack = [-1]
        ## each loop: make sure all heights in stack >= current heights[i]
        
        ## If the height at stack[-1] is bigger than current height[i]
        ## then the width of height[stack[-1] starts at stack[-2] ends at stack[-1]
        ans = 0
        for i in range(len(height)):
            # print(stack)
            while height[i] < height[stack[-1]]:
                h = height[stack.pop()]
                w = i - stack[-1] - 1
                # print("h*w: ",h*w)
                ans = max(ans, h * w)
            stack.append(i)
            # print(stack)
        height.pop()
        return ans


    def largestRectangleArea_test(self, heights: List[int]) -> int:
        ## for each height[i]
        ## move from i to the left till you find first l such that height[l] < height[i] (all other bars l+1,.. i having height >= height[i])
        ## move from i to the right till you find first r such that height[r] < height[i] (all other bars i, ..., r-1 having height >= height[i])
        ## so height i is the shortest bar forming the block
        ## area = (r - l - 1) * height[i]
        
        leftIdx = [0]*len(heights) ## leftIdx[i] := l on left of heights[i]
        leftIdx[0] = -1
        rightIdx = [0]*len(heights) ## rightIdx[i] := r on right of heights[i]
        rightIdx[-1] = -1
        
        i = 1
        while i < len(heights) and heights[i] >= heights[i-1]:
            i += 1
        
        
        
    def largestRectangleArea_compute_height_everytime(self, heights: List[int]) -> int:

        ## for each height[i]
        ## move from i to the left till you find first l such that height[l] < height[i] (all other bars l+1,.. i having height >= height[i])
        ## move from i to the right till you find first r such that height[r] < height[i] (all other bars i, ..., r-1 having height >= height[i])
        ## so height i is the shortest bar forming the block
        ## area = (r - l - 1) * height[i]
        ans = 0
        for i in range(0,len(heights)):
            if i > 0 and heights[i] == heights[i-1]: continue
            l = i
            r = i
            while l >=  0 and heights[l]>=heights[i]:
                l -= 1
            while r < len(heights) and heights[r]>=heights[i]:
                r += 1
                
            ans = max(ans, (r - l - 1) * heights[i])
            
        return ans