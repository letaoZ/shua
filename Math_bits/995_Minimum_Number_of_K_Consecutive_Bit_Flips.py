'''
995. Minimum Number of K Consecutive Bit Flips
Hard

757

47

Add to List

Share
You are given a binary array nums and an integer k.

A k-bit flip is choosing a subarray of length k from nums and simultaneously changing every 0 in the subarray to 1, and every 1 in the subarray to 0.

Return the minimum number of k-bit flips required so that there is no 0 in the array. If it is not possible, return -1.

A subarray is a contiguous part of an array.

 

Example 1:

Input: nums = [0,1,0], k = 1
Output: 2
Explanation: Flip nums[0], then flip nums[2].
Example 2:

Input: nums = [1,1,0], k = 2
Output: -1
Explanation: No matter how we flip subarrays of size 2, we cannot make the array become [1,1,1].
Example 3:

Input: nums = [0,0,0,1,0,1,1,0], k = 3
Output: 3
Explanation: 
Flip nums[0],nums[1],nums[2]: nums becomes [1,1,1,1,0,1,1,0]
Flip nums[4],nums[5],nums[6]: nums becomes [1,1,1,1,1,0,0,0]
Flip nums[5],nums[6],nums[7]: nums becomes [1,1,1,1,1,1,1,1]
 

Constraints:

1 <= nums.length <= 105
1 <= k <= nums.length
'''
class Solution:
    
    def minKBitFlips_dff(self, nums: List[int], k: int) -> int:
        if not (0 in nums): 
            return 0
        ## when we flip k numbers, it is lie nums[i]+1,... nums[i+k-1]+1;
        ## then the diff will only change at nums[i] and nums[i+k]
        ## then we can recover the original nums by keeping on adding it back
        cnt = 0
        dff = [nums[0]] + [nums[i]-nums[i-1] for i in range(1,len(nums))] + [0]## cushion
        psum = 0
        for i in range(len(nums)):
            psum += dff[i]
            if (psum % 2): continue
            if i+k-1 > len(nums) - 1: return -1 ## cannot flip anymore
            cnt += 1
            dff[i] += 1 ## one more flipt
            dff[i+k] -= 1
            psum += 1
        return cnt

    
    def minKBitFlips_window(self, nums: List[int], k: int) -> int:
        if not (0 in nums): 
            return 0
        
        ## flip_record[i] = 1 means we flipped at ith position
        flip_record = [0]*(len(nums))
        
        ## keep track of num of flip within a window k
        ## if we move into a new window, we need to reset it
        flipped = 0
        
        res = 0
        
        for i in range(len(nums)):
            n = nums[i]
            if i>=k:
                ## make sure we reset to new window
                ## flipped was keeping track of window:i-k to i - 1; 
                ## now we move to a new window starting at i; we need to get ride of the impact at i-k
                ## if flip_record[i-k] == 0: flipped = 1 or 0 won't be changed
                ## if flip_record[i-k] == 1: then we need to get ride of the impact at record i-k
                ##      if flip == 1 --> 0; flip == 0 --> 1
                flipped ^= flip_record[i-k] 
            ## we need to flip if nums[i] == 0 and num of flip is even i.e. flipped = 0
            ## we need to flip if nums[i] == 1 and num of flip is odd i.e. flipped = 1
            if flipped == nums[i]:
                if i+k-1>=len(nums): ## we can flip i only if we have more than k elts left
                    return -1
                flip_record[i] = 1#flip
                flipped ^= 1 ## use the 1-->0 and 0--1 trick by xor
                
                res += 1
                
        return res
    
    
    def minKBitFlips_brutal(self, nums: List[int], k: int) -> int:
        ## slow but works
        if not (0 in nums): 
            return 0
        
        i = 0
        res = 0
        while i< len(nums): ## flip from the first 0 you see
            n = nums[i]
            if n == 1:
                pass
            ## if n == 0 we flip from i to i+k-1
            elif i+k-1<len(nums):
                for j in range(i,i+k):
                    nums[j] = (-nums[j] + 1)
                res += 1
            else:
                return -1
            
            i += 1
            # print(nums)
        return res 