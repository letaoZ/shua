'''
2098. Subsequence of Size K With the Largest Even Sum
Medium

9

0

Add to List

Share
You are given an integer array nums and an integer k. Find the largest even sum of any subsequence of nums that has a length of k.

Return this sum, or -1 if such a sum does not exist.

A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.

 

Example 1:

Input: nums = [4,1,5,3,1], k = 3
Output: 12
Explanation:
The subsequence with the largest possible even sum is [4,5,3]. It has a sum of 4 + 5 + 3 = 12.
Example 2:

Input: nums = [4,6,2], k = 3
Output: 12
Explanation:
The subsequence with the largest possible even sum is [4,6,2]. It has a sum of 4 + 6 + 2 = 12.
Example 3:

Input: nums = [1,3,5], k = 1
Output: -1
Explanation:
No subsequence of nums with length 1 has an even sum.
 

Constraints:

1 <= nums.length <= 105
0 <= nums[i] <= 105
1 <= k <= nums.length
'''

class Solution:
    
    def largestEvenSum(self, nums: List[int], k: int) -> int:
        nums.sort(key=lambda x:-x)
        res = sum(nums[:k])
        if res%2 == 0:
            return res
        ## if res is odd, then we either replace the smallest even in top k elts with largest odd in the remaining elements
        ##                        or replace the smallest odd with the largest even the in the remaining elts
        
        ## first find smallest odd and even in the first k elements
        k_even_min = float('inf')
        k_odd_min = float('inf')
        for a in nums[:k][::-1]:
            if k_odd_min>= float('inf') and a%2 == 1:
                k_odd_min = a
            if k_even_min>= float('inf') and a%2 == 0:
                k_even_min = a
            if k_odd_min<float('inf') and k_even_min<float('inf'):
                break

        ## then find largest odd and even in the rest k elements
        rest_k_even_max = -float('inf')
        rest_k_odd_max = -float('inf')
        for a in nums[k:]:
            if rest_k_odd_max<= -float('inf') and a%2 == 1:
                rest_k_odd_max = a
            if rest_k_even_max <= -float('inf') and a%2 == 0:
                rest_k_even_max = a
            if rest_k_odd_max>-float('inf') and rest_k_even_max>-float('inf'):
                break
                
        res_replace_even_min = -float('inf')
        if k_even_min != float('inf') and rest_k_odd_max!=-float('inf'):
            res_replace_even_min = res - k_even_min + rest_k_odd_max

        res_replace_odd_min = -float('inf')

        if k_odd_min != float('inf') and rest_k_even_max != -float('inf'):
            res_replace_odd_min = res - k_odd_min + rest_k_even_max
            
        res = max(res_replace_even_min,res_replace_odd_min)
        return res if res!=-float('inf') else -1
        
        
    def largestEvenSum_DO_NOT_WOR(self, nums: List[int], k: int) -> int:
        
        
        ## divide the nums into even/odd list
        ## to get an even sum you need (even nums) of odd num
        ## zero will contribute to filling up k
        
        nums_even = [n for n in nums if n%2 == 0 and n>=0]
        nums_odd = [n for n in nums if n%2 == 1]
        
        ## special case:
        if k==1:
            if len(nums_even) > 0:
                return max(nums_even)
            else:
                return -1
        
        
        ## special case:
        if len(nums_odd) == 0:
            res = 0
            nums_even = [-t for t in nums_even]
            heapq.heapify(nums_even)
            while k>0 and nums_even:
                res += heapq.heappop(nums_even)
                k -= 1
            if k>0:
                return -1
            else:
                return -res

        ## special case:
        if len(nums_even) == 0:
            if k%2 == 1:
                return -1
            
        ## special case:
        if k>(len(nums_even) + 2*(len(nums_odd)//2) ):
            return -1
        
        ## time = nlog(n)
        nums_odd.sort(key= lambda x:-x)
        
        ## to use odd numbers, they have weight 2
        nums_odd = [nums_odd[i-1]+nums_odd[i] for i in range(1,len(nums_odd),2)]
        
        
        ## knapsack: maximize value where weight is k, each value can only be used once
        values = nums_even + nums_odd
        weights = [1]*len(nums_even) + [2]*len(nums_odd)
        dp = [0]*(k+1)
        print(values)
        print(weights)
        W = k
        ## time = n*k
        if 0 not in values:
            achievable = [0]*(k+1)
            for i,v in enumerate(values):
                w = weights[i]
                achievable[w] = True
                for wi in range(W,w-1,-1):
                    dp[wi] = max(dp[wi],(dp[wi-w] + v)*(dp[wi-w] >0 or wi==w) )
                print(f"i: {i}, v:{v}")
                print(W,dp[W])
                print(dp)
                print(achievable)
                print() 

        # for i in range(len(dp)):
        #     print(i,", ",dp[i])
        print(dp)
        return dp[k]