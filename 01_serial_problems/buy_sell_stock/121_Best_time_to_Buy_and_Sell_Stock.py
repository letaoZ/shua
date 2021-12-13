'''
121. Best Time to Buy and Sell Stock
Easy

12472

451

Add to List

Share
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

 

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
 

Constraints:

1 <= prices.length <= 105
0 <= prices[i] <= 104'''

class Solution:
    def maxProfit_detailed(self, prices: List[int]) -> int:
        res = 0
        left_idx = 0
        right_idx = 0
        cur_left_min = prices[0]
        
        N = len(prices)
        
        while left_idx < N-1:
            while left_idx < N-1 and prices[left_idx] >= prices[left_idx+1]:
                left_idx += 1

            right_idx = left_idx + 1
            if right_idx >= N:
                break

            while right_idx < N-1 and prices[right_idx]<=prices[right_idx+1]:
                right_idx += 1

            cur_left_min = min(cur_left_min, prices[left_idx])
            res = max(res, prices[right_idx] - cur_left_min)

            left_idx = right_idx + 1
            
        return res
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices)<=1: return 0
        
        ## min_price -- keeps on updating
        ## simplified
        min_price = float('inf')
        sz = len(prices)
        l = 1
        res=0
        while l<sz:
            while l<sz and prices[l-1]>=prices[l]:
                l += 1
            min_price=min(min_price,prices[l-1])
            
            while l<sz and prices[l-1]<=prices[l]:
                l += 1
            res = max(res, prices[l-1]-min_price)
        return res
    