'''
546. Remove Boxes
Hard

You are given several boxes with different colors represented by different positive numbers.

You may experience several rounds to remove boxes until there is no box left. 
Each time you can choose some continuous boxes with the same color (i.e., composed of k boxes, k >= 1), remove them and get k * k points.

Return the maximum points you can get.

 

Example 1:

Input: boxes = [1,3,2,2,2,3,4,3,1]
Output: 23
Explanation:
[1, 3, 2, 2, 2, 3, 4, 3, 1] 
----> [1, 3, 3, 4, 3, 1] (3*3=9 points) 
----> [1, 3, 3, 3, 1] (1*1=1 points) 
----> [1, 1] (3*3=9 points) 
----> [] (2*2=4 points)
Example 2:

Input: boxes = [1,1,1]
Output: 9
Example 3:

Input: boxes = [1]
Output: 1

'''








class Solution:## use partial nums as key, to memorize process, still too slow
    def removeBoxes_3d(self, boxes: List[int]) -> int:
        sz = len(boxes)
        dp = [ [ [0]*sz for _ in range(sz)] for _ in range(sz)]
        ## dp[i][j][k] = max score of subarray from box[i] to box[j], where there are k boxes in box[j+1] to box[n] of the same color as box[j]
        ## 注意，这里不管j+1 to n发生了啥，只考虑i to j 且 j与后面的k个相同
        def searching(boxes, l, r, k):
            if l>r: return 0
            if dp[l][r][k] > 0: return dp[l][r][k]
            
            ## 注意，这里不管j+1 to n发生了啥，只考虑i to j 且 j与后面的k个相同
            ## 这个意思就是：我把后面k个都接到了r上，得到k+1个continuously same
            ## 然后remove他们得到l to r-1,这时r-1为最后一个数字
            
            dp[l][r][k] = searching(boxes,l,r-1,0) + (k+1)**2
            for i in range(l,r):
                if boxes[i] == boxes[r]:
                    dp[l][r][k]= max(dp[l][r][k], searching(boxes,l,i,k+1 ) + searching(boxes,i+1,r-1, 0))
            return dp[l][r][k]
        return searching(boxes, 0, sz-1, 0)
        
        
class Solution1:## use partial nums as key, to memorize process, still too slow
    def removeBoxes(self, boxes: List[int]) -> int:
        sz = len(boxes)
        dp = collections.defaultdict(int)
        
        def searching(nums):
            key = tuple(nums)
            if len(nums) <= 1:
                dp[key] = len(nums)
                return len(nums)

            if dp[key]>0:
                return dp[key]
            
            k = 0
            sz = len(nums)
            
            
            k0 = 0
            b0 = nums[k0]
            list_score = []
            while k < sz:
                cnt = 0
                b0 =nums[k0]
                while k<sz and b0 == nums[k]:
                    k += 1
                    cnt += 1
                
                list_score.append(searching(nums[:k0] + nums[k:]) + cnt*cnt)
                k0 = k
            dp[key] = max(list_score)
            return dp[key] 
        searching(boxes)
        
        return dp[tuple(boxes)]
            



class Solution2: ## correct, too slow
    def removeBoxes(self, boxes: List[int]) -> int:
        sz = len(boxes)
        dp = collections.defaultdict()
        
        from functools import lru_cache
        lru_cache(0)
        def searching(nums,cur_score,list_score):
            if len(nums) <= 1:
                list_score.append(cur_score + len(nums))
                return
            k = 0
            sz = len(nums)
            
            
            k0 = 0
            b0 = nums[k0]
            while k < sz:
                cnt = 0
                b0 =nums[k0]
                while k<sz and b0 == nums[k]:
                    k += 1
                    cnt += 1
                
                if k0 == 0:
                    searching(nums[k:],cur_score + cnt*cnt,list_score)
                else:
                    searching(nums[:k0] + nums[k:],cur_score + cnt*cnt,list_score)

                
                k0 = k
            

        list_score =[]
        searching(boxes, 0, list_score)
        
        return max(list_score)
            