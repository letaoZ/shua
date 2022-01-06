'''
774. Minimize Max Distance to Gas Station
Hard

552

78

Add to List

Share
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

class Solution:
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
    def minmaxGasDist_binary_search(self, stations: List[int], k: int) -> float:
        ## min (max_dist {d add k new stations})
        ## given upper bound of max dist
        ## see how many station we need to add
        dist_now = [s2-s1 for s1, s2 in zip(stations, stations[1:])]
        # print(dist_now)
        l, r = 0, max(dist_now) + 1e-6
        while 1e-6<r-l:
            
            
            mid = l + (r-l) / 2.
            cnt_stations = 0
            
            for dd in dist_now:
                if dd<=mid:
                    continue
                elif dd>mid:
                    n_d = dd/mid
                    # print(n_d)
                    if n_d == int(n_d):
                        cnt_stations += (int(n_d)-1)
                    else:
                        cnt_stations += (int(n_d))
            # print(l,mid,r)
            # print(cnt_stations)
            # print()
            if cnt_stations > k: ## increase travel distance to lower the num stations
                l = mid 
            elif cnt_stations < k: ## we can have more stations, and decrease travel
                r = mid
            elif cnt_stations == k: ## we may decrease travel with the same num of stations
                r = mid
        return l
            