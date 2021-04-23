
import collections
## if you want to return all potential sums
## use:         psums = collections.defaultdict(list)
## keep track all indices with the psum
## 


class Solution:
    def subarraySum_slow(self, nums: [int], k: int):
        ## method 1: partial sum difference
        sz = len(nums)
        psum = [0]*(sz + 1)


        res = 0
        for i in range(1, sz+1):
            psum[i] = psum[i-1] + nums[i-1]

        for i in range(1, sz+1):
            for j in range(i, sz+1):
                d = psum[j] - psum[i-1]
                if d == k: res += 1

        return res
    def subarraySum_with_if(self, nums: [int], k: int):

        sz = len(nums)
        psums = collections.defaultdict(int)
        cur_sum = 0
        res = 0
        for i in range(1,1+sz):
            cur_sum += nums[i-1]
            res += psums[cur_sum - k]
            psums[cur_sum] += 1

            if cur_sum == k:
                res += 1
        print(psums)
        return res
                

    def subarraySum_simplify_if(self, nums: [int], k: int):

        
        
        sz = len(nums)
                
        psums = collections.defaultdict(int)
        psums[0] = 1
        cur_sum = 0
        res = 0
        for i in range(1,1+sz):
            cur_sum += nums[i-1]
            res += psums[cur_sum - k]
            psums[cur_sum] += 1
            ## replace the if statement with
            ## assign psums[0] = 1

            # if cur_sum == k:
                # res += 1
        return res

solu = Solution()

nums = [1,1,1,1]
# nums = [1,2,1,3]
# nums  = [1]
k=2
solu.subarraySum(nums,k)