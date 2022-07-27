'''
149. Max Points on a Line
Hard

1330

219

Add to List

Share
Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane, return the maximum number of points that lie on the same straight line.

 

Example 1:


Input: points = [[1,1],[2,2],[3,3]]
Output: 3
Example 2:


Input: points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
Output: 4
 

Constraints:

1 <= points.length <= 300
points[i].length == 2
-104 <= xi, yi <= 104
All the points are unique.

'''
import collections
from typing import *
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        ## use a dictionary: key = slop and points of the slop
        
        d = collections.defaultdict(set)
        
        for j in range(len(points)-1):
            x0,y0 = points[j]
            i = j + 1
            ## use: 'N' to denote vertical line
            # print("x0,y0 : ", x0, y0)
            while i < len(points):
                # print("other: ", points[i])
    
                if x0 - points[i][0] == 0:
                    label = ('H', x0, None)
                else:
                    k = round( (y0 - points[i][1]) / (x0 - points[i][0]) , 6)
                    if k == 0:
                        label = ('V', y0, None)
                    else:
                        label =('S', k, y0 - k*x0)
                # print("label: ", label)
                # d[label].append((x0,y0))
                d[label].add(tuple(points[i]))
                i += 1
            # print()
        res = 0
        # (points.sort())
        # print(points)
        for _, l in d.items():
            # print(_)
            # print(l)
            res = max(res, len(l))
            
        return res + 1