'''
1231. Divide Chocolate
Hard

625

42

Add to List

Share
You have one chocolate bar that consists of some chunks. Each chunk has its own sweetness given by the array sweetness.

You want to share the chocolate with your k friends so you start cutting the chocolate bar into k + 1 pieces using k cuts, each piece consists of some consecutive chunks.

Being generous, you will eat the piece with the minimum total sweetness and give the other pieces to your friends.

Find the maximum total sweetness of the piece you can get by cutting the chocolate bar optimally.

 

Example 1:

Input: sweetness = [1,2,3,4,5,6,7,8,9], k = 5
Output: 6
Explanation: You can divide the chocolate to [1,2,3], [4,5], [6], [7], [8], [9]
Example 2:

Input: sweetness = [5,6,7,8,9,1,2,3,4], k = 8
Output: 1
Explanation: There is only one way to cut the bar into 9 pieces.
Example 3:

Input: sweetness = [1,2,2,1,2,2,1,2,2], k = 2
Output: 5
Explanation: You can divide the chocolate to [1,2,2], [1,2,2], [1,2,2]
 

Constraints:

0 <= k < sweetness.length <= 104
1 <= sweetness[i] <= 105
'''

class Solution:
    def maximizeSweetness(self, sweetness: List[int], k: int) -> int:
        if k == len(sweetness) - 1:
            return min(sweetness)
        if k == 0:
            return sum(sweetness)
        
        
        ## the most you can get is M = sum(sweetness) // (k+1)
        ## if everyone gets more than M, then (k+1)*M > sum(sweetness), wrong!
        ## I can get at least min(sweetness)
        
        M = sum(sweetness) // (k+1)
        
        l, r = min(sweetness), M
        
        res = l
        while l<=r:
            mid = l + (r-l)//2
            cnt = 0 ## count number of cuts so far
            tmp = 0 ## count each pile 
            res = float("inf")
            # print("l: ", l)
            # print("mid: ", mid)
            ## mid stands for the possible MIN value of subsum, i.e. our sum
            
            for ss in sweetness:
                tmp += ss
                if tmp >= mid: ## the person gets more than mid, then that's the max the person gets
                    cnt += 1
                    res = min(res, tmp)
                    tmp = 0
                
            if cnt == k+1 and res == mid:
                # print("cnt: ",cnt)
                # print("res: ", res)
                # print("mid: ", mid)
                return res
            elif cnt == k+1 and res!=mid:
                l = res
            elif cnt > k+1:## means we can get more than mid
                l = max(res, mid + 1)
                
            elif cnt < k + 1: ## means we can't get mid
                r = mid - 1
            # print()
        # print("l: ", l)
        # print("r: ",r)
        # print("res: ", res)
        return res
                
                
                    
            
        