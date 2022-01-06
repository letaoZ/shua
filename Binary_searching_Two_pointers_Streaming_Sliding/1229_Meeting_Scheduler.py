'''
1229. Meeting Scheduler
Medium

555

23

Add to List

Share
Given the availability time slots arrays slots1 and slots2 of two people and a meeting duration duration, return the earliest time slot that works for both of them and is of duration duration.

If there is no common time slot that satisfies the requirements, return an empty array.

The format of a time slot is an array of two elements [start, end] representing an inclusive time range from start to end.

It is guaranteed that no two availability slots of the same person intersect with each other. That is, for any two time slots [start1, end1] and [start2, end2] of the same person, either start1 > end2 or start2 > end1.

 

Example 1:

Input: slots1 = [[10,50],[60,120],[140,210]], slots2 = [[0,15],[60,70]], duration = 8
Output: [60,68]
Example 2:

Input: slots1 = [[10,50],[60,120],[140,210]], slots2 = [[0,15],[60,70]], duration = 12
Output: []
 

Constraints:

1 <= slots1.length, slots2.length <= 104
slots1[i].length, slots2[i].length == 2
slots1[i][0] < slots1[i][1]
slots2[i][0] < slots2[i][1]
0 <= slots1[i][j], slots2[i][j] <= 109
1 <= duration <= 106
'''

class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        ## remove all slots that's less than duration
        
        slots1 = [[a,b] for a,b in slots1 if b-a >= duration]

        slots2 = [[a,b] for a,b in slots2 if b-a >= duration]
        
        if len(slots1) == 0 or len(slots2) == 0:
            return []
        
        slots1.sort(key = lambda x:(x[0],x[1]) )
        
        slots2.sort(key = lambda x:(x[0],x[1]) )
        
        i1, i2 = 0, 0
        while i1<len(slots1) and i2<len(slots2):
            l1,r1 = slots1[i1]
            l2,r2 = slots2[i2]
            # print(f"l1, r1: {l1,r1}")
            # print(f"l2, r2: {l2,r2}")
            start = max(l1,l2)
            end  = min(r1,r2)
            if end-start >= duration:
                return [start, start + duration]
            else:
                ## crutial!! 
                ## update following "ending time"
                if r1 < r2:
                    i1 += 1
                elif r1 > r2:
                    i2 += 1
                elif r1 == r2:
                    i1 += 1
                    i2 += 1
                
            
        
        return []