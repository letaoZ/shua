'''
152. Maximum Product Subarray
Medium

Given an integer array nums, find a contiguous non-empty subarray within the array that has the largest product, and return the product.

It is guaranteed that the answer will fit in a 32-bit integer.

A subarray is a contiguous subsequence of the array.

 

Example 1:

Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:

Input: nums = [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
 

Constraints:

1 <= nums.length <= 2 * 104
-10 <= nums[i] <= 10
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

'''

'''
Insights:
A: What if the array has just positive numbers including zero?
A solution of this will maintain max_prod[i] where max_prod[i] is the maximum subarray product ending at i. 
Then max_prod[i+1] = max(max_prod[i] * nums[i+1], nums[i+1]).
B: Now how do we change the solution when we allow negative numbers?
Imagine that we have both max_prod[i] and min_prod[i] 
i.e. max prod ending at i and min prod ending at i. 
Now if we have a negative number at nums[i+1] and if min_prod[i] is negative, 
then the product of the two will be positive and can potentially be largest product. 
Key point is to maintain both max_prod and min_prod such that at iteration i, they refer to the max and min prod ending at index i -1.
You have three choices to make at any position in array.

You can get maximum product by multiplying the current element with
maximum product calculated so far. (might work when current
element is positive).
You can get maximum product by multiplying the current element with
minimum product calculated so far. (might work when current
element is negative).
Current element might be a starting position for maximum product sub
array

'''

class Solution:
    def maxProduct_slowDP(self, nums: List[int]) -> int:
        
        ## three special values:0,negative, positive
        ## 1. if there are zeros, the max is either zero or things after zero, depending on number of negative values after zero
        ## 1. if there are no zeros, find the first place
        
        sz = len(nums)
        prods = [[0]*(sz+1) for _ in range(sz+1)]
        prods[0][0] = 1
        res = max(nums)
        for i in range(1,sz+1):
            prods[i][i] = nums[i-1]
            if nums[i-1] != 0: 
                for j in range(i+1,sz+1):
                    prods[i][j] = nums[j-1]*prods[i][j-1]
                    res = max(res,prods[i][j])
                    if prods[i][j] == 0:
                        break
                        
        return res
                        
    def maxProduct_minMax_noSwap(self, nums) -> int:
        sz = len(nums)
        res = max(nums)
        min_prod = 1
        max_prod = 1

        for i in range(sz):
            min_prod_tmp = min(nums[i],nums[i]*min_prod,nums[i]*max_prod)
            max_prod_tmp = max(nums[i],nums[i]*max_prod,nums[i]*min_prod)
            res = max(res, max_prod_tmp)
            min_prod, max_prod = min_prod_tmp, max_prod_tmp

        return (res)
        
    def maxProduct_minMax_noSwap_slightly_improve(self, nums) -> int:
        ## improve noSwap by referencing nums' elts, instead of indices
        sz = len(nums)
        min_prod = max_prod = res =nums[0]
        for n in nums[1:]:
            min_prod_tmp = min(n,n*min_prod,n *max_prod)
            max_prod_tmp = max(n,n*max_prod,n *min_prod)
            res = max(res, max_prod_tmp)
            min_prod, max_prod = min_prod_tmp, max_prod_tmp

        return (res)
    
    

    def maxProduct_ultimate_solution(self, nums) -> int:        

        if min(nums)>0:
            p  = 1
            for n in nums:
                p*=n
            return p
        
        #  res: store the result that is the max we have found so far
        #  min_prod/max_prod: stores the max/min product of subarray that ends with the current number result[i]
        
        
        sz = len(nums)
        min_prod = max_prod = res = nums[0]

        for num in nums[1:]:
        # // multiplied by a negative makes big number smaller, small number bigger
        # // so we redefine the extremums by swapping them
            if num<0:
                min_prod, max_prod = max_prod, min_prod
                
        # Not, include the num here is to deal with previous prods are zeros. So this case we will initiate a partial prod
        ## starting at num
            min_prod = min(min_prod*num ,num )
            max_prod = max(max_prod*num ,num )
        ## update global res
            res = max(res, max_prod)
        return res

nums = [2,3,-2,4]
solu = Solution()
solu.maxProduct(nums)