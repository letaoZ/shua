'''
1775. Equal Sum Arrays With Minimum Number of Operations
Medium

432

12

Add to List

Share
You are given two arrays of integers nums1 and nums2, possibly of different lengths. The values in the arrays are between 1 and 6, inclusive.

In one operation, you can change any integer's value in any of the arrays to any value between 1 and 6, inclusive.

Return the minimum number of operations required to make the sum of values in nums1 equal to the sum of values in nums2. Return -1​​​​​ if it is not possible to make the sum of the two arrays equal.

 

Example 1:

Input: nums1 = [1,2,3,4,5,6], nums2 = [1,1,2,2,2,2]
Output: 3
Explanation: You can make the sums of nums1 and nums2 equal with 3 operations. All indices are 0-indexed.
- Change nums2[0] to 6. nums1 = [1,2,3,4,5,6], nums2 = [6,1,2,2,2,2].
- Change nums1[5] to 1. nums1 = [1,2,3,4,5,1], nums2 = [6,1,2,2,2,2].
- Change nums1[2] to 2. nums1 = [1,2,2,4,5,1], nums2 = [6,1,2,2,2,2].
Example 2:

Input: nums1 = [1,1,1,1,1,1,1], nums2 = [6]
Output: -1
Explanation: There is no way to decrease the sum of nums1 or to increase the sum of nums2 to make them equal.
Example 3:

Input: nums1 = [6,6], nums2 = [1]
Output: 3
Explanation: You can make the sums of nums1 and nums2 equal with 3 operations. All indices are 0-indexed. 
- Change nums1[0] to 2. nums1 = [2,6], nums2 = [1].
- Change nums1[1] to 2. nums1 = [2,2], nums2 = [1].
- Change nums2[0] to 4. nums1 = [2,2], nums2 = [4].
 

Constraints:

1 <= nums1.length, nums2.length <= 105
1 <= nums1[i], nums2[i] <= 6
'''
import collections
import itertools
class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        if len(nums1) * 6 < len(nums2) or len(nums2) * 6 < len(nums1):
            return -1
        
        s1 = sum(nums1)
        s2 = sum(nums2)
        if s1 == s2:
            return 0
        
        
        if s1 < s2:
            # s1, s2 = s2, s1
            # nums1, nums2 = [_ for _ in nums2],  [_ for _ in nums1]
            return self.minOperations(nums2, nums1)
        nums1.sort()
        nums2.sort()
        
        d = s1 - s2
        cnt = 0
        i1, i2 = len(nums1)-1, 0
        
        ## each step either increase smaller the most or decrease larger the most
        ## decrease nums1, increase nums2
        while d>0 and (i1>=0 or i2<len(nums2)):
            delta1 = delta2 = delta = 0
            
            if i1 >= 0:
                delta1 = nums1[i1] - 1
            if i2 < len(nums2):
                delta2 = 6 - nums2[i2]

            if delta1 > delta2 or (delta1 == delta2 and delta1>0):
                delta = min(d,delta1)
                # nums1[i1] -= delta
                i1 -= 1
            elif delta1 < delta2:
                delta = min(d,delta2)
                # nums2[i2] += delta
                i2 += 1
            elif delta1 == delta2 == 0:
                i1 -= 1
                i2 += 1
            # print(d)
            # print(nums1)
            # print(nums2)
            # print()
            if delta > 0:
                cnt += 1
            d -= delta
            
        if d>0:
            return -1
        else:
            return cnt
        
        
        
    def minOperations_simplify(self, nums1: List[int], nums2: List[int]) -> int:
        if len(nums1) * 6 < len(nums2) or len(nums2) * 6 < len(nums1):
            return -1
        s1, s2 = sum(nums1), sum(nums2)

        if s1 < s2:
            return self.minOperations(nums2, nums1)
        
        
        ## idea is similar:
        ## each step either increase smaller the most or decrease larger the most
        ## either way we are subtracteing from the difference
        ## so we can combine the two nums together
        
        counter = [num - 1 for num in nums1 if num - 1 > 0]
        counter += [6 - num  for num in nums2 if 6 - num > 0]
        
        counter.sort(key = lambda x:-x)

        d = s1 - s2
        cnt = 0
        while d > 0 and cnt < len(counter):
            d -= counter[cnt]
            cnt += 1
            
        if d <= 0:
            return cnt
        return -1


    def minOperations_simplify_counter(self, nums1: List[int], nums2: List[int]) -> int:
        if len(nums1) * 6 < len(nums2) or len(nums2) * 6 < len(nums1):
            return -1
        s1, s2 = sum(nums1), sum(nums2)
        
        if s1 == s2:
            return 0
        if s1 < s2:
            return self.minOperations(nums2, nums1)
        
        
        ## idea is similar:
        ## each step either increase smaller the most or decrease larger the most
        ## either way we are subtracteing from the difference
        ## so we can combine the two nums together
        ## we can use itertools and counter
        
        counter = collections.Counter([num - 1 for num in nums1 if num - 1 > 0])
        counter += collections.Counter([6 - num  for num in nums2 if 6 - num > 0])
        d = s1 - s2
        cnt = 0
        
        # print(counter,d)
        for k in range(5,0,-1):
            if k not in counter:
                continue
            cntk = counter[k]
            while d>0 and cntk>0:
                d -= k
                cntk -= 1
                cnt += 1
            if d<=0:
                return cnt
        
        return -1
    
    
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        if len(nums1) * 6 < len(nums2) or len(nums2) * 6 < len(nums1):
            return -1
        s1, s2 = sum(nums1), sum(nums2)
        if s1 > s2: return self.minOperations(nums2, nums1)
        counter = collections.Counter(6 - num for num in nums1 if num<6)
        counter += collections.Counter(num - 1 for num in nums2 if num > 1)
        ops = 0
        I = itertools.chain.from_iterable(
            itertools.repeat(i, counter[i]) for i in reversed(range(1, 6)))
        while s1 < s2:
            s1 += next(I)
            ops += 1
        return ops
