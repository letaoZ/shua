'''
1094. Car Pooling
Medium

2940

64

Add to List

Share
There is a car with capacity empty seats. The vehicle only drives east (i.e., it cannot turn around and drive west).

You are given the integer capacity and an array trips where trips[i] = [numPassengersi, fromi, toi] indicates that the ith trip has numPassengersi passengers and the locations to pick them up and drop them off are fromi and toi respectively. The locations are given as the number of kilometers due east from the car's initial location.

Return true if it is possible to pick up and drop off all passengers for all the given trips, or false otherwise.

 

Example 1:

Input: trips = [[2,1,5],[3,3,7]], capacity = 4
Output: false
Example 2:

Input: trips = [[2,1,5],[3,3,7]], capacity = 5
Output: true
 

Constraints:

1 <= trips.length <= 1000
trips[i].length == 3
1 <= numPassengersi <= 100
0 <= fromi < toi <= 1000
1 <= capacity <= 105
'''
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        ## find max overlap
        
        N = max([r[2] for r in trips])
        
        dff = [0]*(N + 2)
        for (num,b,e) in trips:
            dff[b] += num
            dff[e-1+1] -= num ## at e, ppl already got off
        mx = dff[0]
        for i in range(1,N+1):
            dff[i] += dff[i-1]
            mx = max(mx, dff[i])
            # print(i,mx)
            if mx>capacity:
                return False
            
        return True