'''
1014. Best Sightseeing Pair
Medium

1169

31

Add to List

Share
You are given an integer array values where values[i] represents the value of the ith sightseeing spot. Two sightseeing spots i and j have a distance j - i between them.

The score of a pair (i < j) of sightseeing spots is values[i] + values[j] + i - j: the sum of the values of the sightseeing spots, minus the distance between them.

Return the maximum score of a pair of sightseeing spots.

 

Example 1:

Input: values = [8,1,5,2,6]
Output: 11
Explanation: i = 0, j = 2, values[i] + values[j] + i - j = 8 + 5 + 0 - 2 = 11
Example 2:

Input: values = [1,2]
Output: 2
 

Constraints:

2 <= values.length <= 5 * 104
1 <= values[i] <= 1000
'''

class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        ## dp[j], max dist if including val[j]
        N = len(values)
        dp = [-float('inf')]*N
        
        ## time = N^2
        left_end = -1
        new_left = -1
        for j in range(1,N):
            left_end = new_left
            
            for i in range(j-1,left_end-1,-1):
                cur_dist = values[j] + values[i] + i-j
                if dp[j]> cur_dist:
                    continue
                dp[j] = max(dp[j], cur_dist)
                new_left = i
                    
        return max(dp)
    
