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
    def shortestDistanceColor_brutal(self, colors: List[int], queries: List[List[int]]) -> List[int]:
        
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
                    
    def shortestDistanceColor_scan_first(self, colors: List[int], queries: List[List[int]]) -> List[int]:
        ##dp_left[c][idx]: for each index, look at its left: the nearest distance color C
        ## define dp_right similarly
        
        dp_left = [[-1]*len(colors) for _ in range(3+1)]
        dp_right = [[-1]*len(colors) for _ in range(3+1)]
        
        for C in [1,2,3]:
            for idx in range(len(colors)):
                ic = colors[idx]
                if C == ic:
                    dp_left[C][idx] = 0
                else:
                    if idx>0 and dp_left[C][idx-1]>=0:
                        dp_left[C][idx] = dp_left[C][idx-1] + 1
                    
                    

        for C in [1,2,3]:
            for idx in range(len(colors)-1,-1,-1):
                ic = colors[idx]
                if C == ic:
                    dp_right[C][idx] = 0
                else:
                    if idx<len(colors)-1 and dp_right[C][idx+1]>=0:
                        dp_right[C][idx] = dp_right[C][idx+1] + 1
                        
        # print(dp_left[1])
        # print(dp_right[1])
        ## for each query, we can find its left and right dist
        res = [-1]*len(queries)
        for k,(idx,ic) in enumerate(queries):
            left_d = dp_left[ic][idx] 
            right_d = dp_right[ic][idx] 
            if left_d == -1 or right_d == -1:
                res[k] = max(right_d, left_d) 
            else:
                res[k] = min(right_d, left_d)
            
            
        return res