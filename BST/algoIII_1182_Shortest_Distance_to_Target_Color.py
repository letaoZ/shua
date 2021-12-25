'''
1182. Shortest Distance to Target Color
Medium

309

14

Add to List

Share
You are given an array colors, in which there are three colors: 1, 2 and 3.

You are also given some queries. Each query consists of two integers i and c, return the shortest distance between the given index i and the target color c. If there is no solution return -1.

 

Example 1:

Input: colors = [1,1,2,1,3,2,2,3,3], queries = [[1,3],[2,2],[6,1]]
Output: [3,0,3]
Explanation: 
The nearest 3 from index 1 is at index 4 (3 steps away).
The nearest 2 from index 2 is at index 2 itself (0 steps away).
The nearest 1 from index 6 is at index 3 (3 steps away).
Example 2:

Input: colors = [1,2], queries = [[0,3]]
Output: [-1]
Explanation: There is no 3 in the array.
 

Constraints:

1 <= colors.length <= 5*10^4
1 <= colors[i] <= 3
1 <= queries.length <= 5*10^4
queries[i].length == 2
0 <= queries[i][0] < colors.length
1 <= queries[i][1] <= 3'''

class Solution:
    def shortestDistanceColor(self, colors: List[int], queries: List[List[int]]) -> List[int]:
        
        res = [-1]*len(queries)
        res_d = {(a,b):None for a,b in queries}
        for q,(i,c) in enumerate(queries):
            if res_d[(i,c)] is not None:
                res[q] = res_d[(i,c)]
                continue
            if c not in colors:
                continue
            for d in range(0,len(colors)):
                c_l = i-d
                c_r = i+d
                if c_l>=0:
                    if colors[c_l] == c:
                        res[q] = d
                        res_d[(i,c)] = d
                        break
                if c_r<len(colors):
                    if colors[c_r] == c:
                        res[q] = d
                        res_d[(i,c)] = d
                        break
            if res_d[(i,c)] is None:
                res_d[(i,c)] = -1
            
        return res
                    
