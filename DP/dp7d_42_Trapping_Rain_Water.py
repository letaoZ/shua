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
        N = len(height)        
        
        ## remove zeros at front and back
        ## don't have to do this
        i = 0
        while i<N and height[i] == 0:
            i += 1
            
        if i == N:
            return 0
        
        height = height[i:]
        N = len(height)
        i = N-1
        while i>0 and height[i] == 0:
            i -= 1
                
        height = height[:i+1]
        N = len(height)
        
        ## use heights without zeros
        ## queue stores height
        queue = collections.deque([(height[0],0)] )
        start = 1
        res = 0
        prev = None

        while start < N:
            k = start
            while k<N:                
                if height[k] <= height[k-1]:
                    queue.append((height[k],k) )
                else:
                    break
                k += 1
            
            if k == N:
                return res
            
            wall_r = height[k]
            prev, prev_idx = queue.pop()
            # print("queue")
            # print(queue)
            # print("wall_r")
            # print(wall_r)
            # print("prev")
            # print(prev)
            
            while queue:
                prev_l, prev_l_idx = queue.pop()
                if prev_l == prev:
                    continue
                if prev_l <= wall_r:
                    res += (prev_l - prev) * (k - (prev_l_idx+1))
                    prev = prev_l
                    # print("res: ",res)
                else:
                    res += (wall_r - prev) * (k - (prev_l_idx+1))
                    queue.append((prev_l, prev_l_idx))
                    # print(f"wall_r {wall_r}, prev {prev}")
                    # print("break res: ",res)

                    break
            
            queue.append((wall_r,k))
            
            start = k+1
        return res