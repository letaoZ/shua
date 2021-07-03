'''774. Minimize Max Distance to Gas Station
Hard


You are given an integer array stations that represents the positions of the gas stations on the x-axis. You are also given an integer k.

You should add k new gas stations. You can add the stations anywhere on the x-axis, and not necessarily on an integer position.

Let penalty() be the maximum distance between adjacent gas stations after adding the k new stations.

Return the smallest possible value of penalty(). Answers within 10-6 of the actual answer will be accepted.

 

Example 1:

Input: stations = [1,2,3,4,5,6,7,8,9,10], k = 9
Output: 0.50000
Example 2:

Input: stations = [23,24,36,39,46,56,57,65,84,98], k = 1
Output: 14.00000
 

Constraints:

10 <= stations.length <= 2000
0 <= stations[i] <= 108
stations is sorted in a strictly increasing order.
1 <= k <= 106
'''

import heapq
List = list()
class Solution:
    def minmaxGasDist(self, stations: List[int], k: int) -> float:
       ## binary search
       ## for each dist, see if we can use K more station to reach dist
        ## cnt is total station need cnt to <= mid
        
        dlist = (
            [d1-d0 for d0, d1 in zip(stations, stations[1:])])
        # l, r = min(dlist), max(dlist)
        l, r = 0, stations[-1] - stations[0]
        sz = len(stations)
        while r-l>1e-6:
            mid = l + (r-l)/2.
            cnt = 0
            for i in range(sz-1):
                my_d = stations[i+1] - stations[i]
                my_cnt = my_d//mid
                
                cnt += my_cnt
            
            if cnt > k: ## cnt is min you need to reach mid. mid is too big to realize
                l = mid
            else:
                r = mid
        return l
        
    def minmaxGasDist_heap_slow(self, stations: List[int], k: int) -> float:
        ## heap
        
        
        q= [[s0 - s1,s0-s1, 1] for s0, s1 in zip(stations, stations[1:])]
        heapq.heapify(q)
        d = float('inf')
        # print(q)
        while q and k>0:
            
            dm,d0,dn = heapq.heappop(q)
            dm *= -1
            
            d = min(d, dm)
            dm = d0/(dn+1)
            heapq.heappush(q, [dm, d0, dn+1])
            k -= 1
            # print(q)
        
        if q:
            dm,_,_ = heapq.heappop(q)
            d = min(d, -dm)
        
        return d