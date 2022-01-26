'''
4. Median of Two Sorted Arrays
Hard

14503

1828

Add to List

Share
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

 

Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
 

Constraints:

nums1.length == m
nums2.length == n
0 <= m <= 1000
0 <= n <= 1000
1 <= m + n <= 2000
-106 <= nums1[i], nums2[i] <= 106
'''

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
         ## we always assume len(nums1) <= len(nums2)
        if len(nums1)>len(nums2):
            nums1, nums2 = nums2, nums1
            
        N1, N2 = len(nums1), len(nums2)
        
        ## number of elts to cut in the new sequence. 
        # eg. N1 = 2, N2 = 4; then new sequence length 6, at least 3 elts on the left: index 2,3
        # eg. N1 = 1, N2 = 4; then  new sequence length 5,at least 3 elts on the left: index 2
        cnt_elt = (N1+N2 + 1) // 2 
        
        ## we want to take the first m1 elts from nums1; first m2 elts from nums2; where m1 + m2 = cnt_left
        ## if total is odd many elts,  then the last elt of the sequence nums1[:m1] combined with nums2[:m2] is the median. i.e. max(nums1[m1-1], nums2[m2-1])
        ## if total is even many elts, then the last elt of the sequence nums1[:m1] combined with nums2[:m2] AND the elt after gives median. The elt after is min(nums1[m1], nums2[m2])
        
        ## binary search on m1, nums1:return r --- NOTE: we are able to modify r every time
        ## search condition: we need nums1[m1] > nums2[m2-1]; nums1[m1-1]<nums[m2]
        
        l, r = 0, len(nums1)
        ## [l, r): l,r are length count: left and right bound
        ## we do binary search on COUNT OF ELT IN nums1
        while l<r:
            m1 = l + (r-l)//2 ##cnt
            m2 = cnt_elt - m1  ## cnt
            if nums2[m2-1] <= nums1[m1]:
                r = m1
        
            else:
                l = m1 + 1
        m1 = l
        m2 = cnt_elt - m1
        
        ## max( nums[m1-1], nums[m2-1]) if valid
        nums1_left = -float('inf') if (m1-1)<0 else nums1[m1-1]
        nums2_left = -float('inf') if (m2-1)<0 else nums2[m2-1]
        res_left = max(nums1_left, nums2_left)
        
        print(f"m1: {m1}, m2: {m2}")
        print(f"nums1_left: {nums1_left}, nums2_left: {nums2_left}")
        
        
        if (N1+N2) %2:
            return res_left
        
        ## min( nums[m1], nums[m2]) if valid
        nums1_right = float('inf') if (m1)>=N1 else nums1[m1]
        nums2_right = float('inf') if (m2)>=N2 else nums2[m2]
        res_right = min(nums1_right, nums2_right)
        print(f"nums1_right: {nums1_right}, nums2_left: {nums2_right}")
        
        
        return (res_right + res_left) / 2
        
        
        
    def findMedianSortedArrays_binary_search_too_many_conditions(self, nums1: List[int], nums2: List[int]) -> float:
        ## we always assume len(nums1) <= len(nums2)
        if len(nums1)>len(nums2):
            nums1, nums2 = nums2, nums1
            # self.findMedianSortedArrays(nums2, nums1)
            
        N1, N2 = len(nums1), len(nums2)
        n_left = (N1+N2-1) // 2  ## index
        n_right = (N1 + N2) // 2 ## index  
        # print(n_left, n_right)
        
        ## boundary cases: 
        ## we don't need nums1
        if N1 == 0:
            return (nums2[n_left] + nums2[n_right]) / 2

        if  nums1[-1] <= nums2[0]:
            if N1 == N2:
                return (nums1[-1] + nums2[0]) / 2
            else:
                n_left -= N1
                n_right -= N1
                return (nums2[n_left] + nums2[n_right]) / 2

        if nums1[0]>=nums2[-1]:
            if N1 == N2:
                return (nums1[0] + nums2[-1]) / 2
            else:
                return (nums2[n_left] + nums2[n_right]) / 2

        
        ## number of elts to cut in the new sequence. 
        # eg. N1 = 2, N2 = 4; then at least 3 elts on the left: index 2,3
        # eg. N1 = 1, N2 = 4; then at least 3 elts on the left: index 2
        cnt_elt = (N1+N2 + 1) // 2 
        
        ## we want to take the first m1 elts from nums1; first m2 elts from nums2; where m1 + m2 = cnt_left
        ## if n_left == n_right, then the last elt of the sequence nums1[:m1] combined with nums2[:m2] is the median. i.e. max(nums1[m1-1], nums2[m2-1])
        ## if n_left < n_right, then the last elt of the sequence nums1[:m1] combined with nums2[:m2] AMD the elt after gives median. The elt after is min(nums1[m1], nums2[m2])
        
        ## binary search on m1, nums1:return r --- NOTE: we are able to modify r every time
        ## search condition: we need nums1[m1] > nums2[m2-1]; nums1[m1-1]<nums[m2]
        
        l, r = 0, len(nums1)
        ## [l, r): l,r are count left and right bound
        ## we do binary search on COUNT OF ELT IN nums1
        while l<r:
            m1 = l + (r-l)//2 ##cnt
            m2 = cnt_elt - m1  ## cnt
            if nums2[m2-1] <= nums1[m1]:
                r = m1
            else:
                l = m1 + 1
        m1 = l
        m2 = cnt_elt - m1
        
        
        print("m1 ", m1)
        print("m2 ", m2)
        print(n_left, n_right)
        if m1 <= 0:
            if n_left == n_right:
                return nums2[m2-1]
            else:
                if m1 == 0:
                    res_right = min(nums1[m1], nums2[m2])
                else:
                    res_right = nums2[m2]
                return (nums2[m2 - 1] + res_right) / 2
        
        elif m2 <= 0:
            if n_left == n_right:
                return nums1[m1-1]
            else:
                if m2 == 0:
                    res_right = min(nums1[m1], nums2[m2])
                else:
                    res_right = nums1[m1]
                return (nums1[m1 - 1] + res_right) / 2
        else:
            left_res = max(nums1[m1-1], nums2[m2-1])
            if n_left == n_right:
                return left_res
            else:
                if m1>=N1:
                    right_res = nums2[m2]
                elif m2>=N2:
                    right_res = nums1[m1]
                else:
                    right_res = min(nums1[m1],nums2[m2])
                return (left_res + right_res)/2
        
        
    def findMedianSortedArrays_brutal(self, nums1: List[int], nums2: List[int]) -> float:
        ## brutal
        N1, N2 = len(nums1), len(nums2)

        if len(nums1) == 0:
            return nums2[len(nums2)//2]
        
        cnt = len(nums1) + len(nums2)
        mid1 = cnt//2
        mid2 = (cnt-1) //2
        
        res1 = None
        res2 = None
        
        i1 = i2 = 0
        # print(mid1, mid2)
        cnt = 0
        while cnt<=mid1:
            if (i2 >= N2) or (i1<N1 and nums1[i1]<=nums2[i2]):
                if cnt == mid2:
                    res2 = nums1[i1]
                if cnt == mid1:
                    res1 = nums1[i1]
                i1 += 1
            elif (i1>=N1) or (i2<N2 and nums1[i1]>nums2[i2]):
                if cnt == mid2:
                    res2 = nums2[i2]
                if cnt == mid1:
                    res1 = nums2[i2]
                i2 += 1
                
            cnt += 1
                
        return (res1 + res2) / 2
        