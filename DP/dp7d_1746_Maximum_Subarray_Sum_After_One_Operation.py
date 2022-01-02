class Solution:
    def maxSumAfterOperation(self, nums: List[int]) -> int:
        prev_sum_no_sq = 0
        prev_sum_w_sq = 0
        res = nums[0]**2
        for n in nums:
            prev_sum_w_sq = max(prev_sum_no_sq + n**2,prev_sum_w_sq + n, n**2)
            prev_sum_no_sq = max(prev_sum_no_sq+n, 0)

            res = max(prev_sum_w_sq,res)
        return res