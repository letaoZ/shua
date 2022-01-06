'''
42. Trapping Rain Water
Hard

15483

221

Add to List

Share
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

 

Example 1:


Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
Example 2:

Input: height = [4,2,0,3,2,5]
Output: 9
 

Constraints:

n == height.length
1 <= n <= 2 * 104
0 <= height[i] <= 105'''



class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) <= 1:
            return 0
        
        queue = collections.deque()
        queue.append((height[0],0))
        res = 0
        i = 1
        ## queue maintain a nonincreasing sequence of heights
        while queue and i< len(height):
            hi = height[i]
            if hi<=height[i-1]:
                queue.append((hi,i))
                i += 1
                continue
                
            ## h_prev means the possible bottom of the water
            h_prev, i_prev = queue[-1]
            
            while queue:
                if h_prev == queue[-1][0]:## extend the bottom of the water
                    _, i_prev = queue.pop()
                    ## NOTE: if len(queue) == 0: no left end to trap water
                
                    continue
                else: ## we have left end to trap water
                    # print(queue)
                    h_left, i_left = queue.pop()
                    delta_h = min(hi, h_left) - h_prev
                    dist = (i - i_left - 1)
                    res += (delta_h*dist)
                    if h_left <= hi:
                        h_prev = h_left
                    else:
                        queue.append((h_left,i_left))
                        break
                            
                            
            queue.append((hi,i))
            i += 1
            # print(f"res {res}")
        return res

