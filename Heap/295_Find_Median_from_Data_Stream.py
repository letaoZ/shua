'''
295. Find Median from Data Stream


The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value and the median is the mean of the two middle values.

For example, for arr = [2,3,4], the median is 3.
For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.
Implement the MedianFinder class:

MedianFinder() initializes the MedianFinder object.
void addNum(int num) adds the integer num from the data stream to the data structure.
double findMedian() returns the median of all elements so far. Answers within 10-5 of the actual answer will be accepted.
 

Example 1:

Input
["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
[[], [1], [2], [], [3], []]
Output
[null, null, null, 1.5, null, 2.0]

Explanation
MedianFinder medianFinder = new MedianFinder();
medianFinder.addNum(1);    // arr = [1]
medianFinder.addNum(2);    // arr = [1, 2]
medianFinder.findMedian(); // return 1.5 (i.e., (1 + 2) / 2)
medianFinder.addNum(3);    // arr[1, 2, 3]
medianFinder.findMedian(); // return 2.0
 

Constraints:

-105 <= num <= 105
There will be at least one element in the data structure before calling findMedian.
At most 5 * 104 calls will be made to addNum and findMedian.
 

Follow up:

If all integer numbers from the stream are in the range [0, 100], how would you optimize your solution?
If 99% of all integer numbers from the stream are in the range [0, 100], how would you optimize your solution?

'''

class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        
        ## assume len of smallest <= len of largest
        self.smallest = []
        self.largest = []

        self.n = 0

    def addNum(self, num: int) -> None:
        ## log(len(num))
        ## If we call addNum N times
        ## time complexity = sum (log n) n=1,..,N ; =O(NlogN)
        ## N! ~ \sqrt(2pi N)(N/e)^N
        if self.n == 0:
            
            heapq.heappush(self.largest, num)
            self.n += 1
            return
        l = self.largest[0]
        if num >= l:
            heapq.heappush(self.largest, num)
        else:
            heapq.heappush(self.smallest, -num)
        
        while len(self.smallest)>len(self.largest):
            heapq.heappush(self.largest,-heapq.heappop(self.smallest))
        while len(self.smallest)<len(self.largest)-1:
            heapq.heappush(self.smallest,-heapq.heappop(self.largest))
        self.n += 1
    def findMedian(self) -> float:

#         print('s: ',self.smallest)
#         print('L: ',self.largest)
        v2 =self.largest[0]
        if self.n%2 == 0:
            v1 = -self.smallest[0]
            return (v1+v2)/2
        else:
            return v2            
    
# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()