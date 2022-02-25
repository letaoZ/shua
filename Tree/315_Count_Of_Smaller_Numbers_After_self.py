'''
Fenwick tree
https://www.youtube.com/watch?v=WbafSgetDDk
'''


'''
315. Count of Smaller Numbers After Self
Hard

5171

150

Add to List

Share
You are given an integer array nums and you have to return a new counts array. 
The counts array has the property where counts[i] is the number of smaller 
elements to the right of nums[i].

 

Example 1:

Input: nums = [5,2,6,1]
Output: [2,1,1,0]
Explanation:
To the right of 5 there are 2 smaller elements (2 and 1).
To the right of 2 there is only 1 smaller element (1).
To the right of 6 there is 1 smaller element (1).
To the right of 1 there is 0 smaller element.
Example 2:

Input: nums = [-1]
Output: [0]
Example 3:

Input: nums = [-1,-1]
Output: [0,0]
 

Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104



'''

class Solution:
    
    def update_tree(self, fenwick_sum, idx, delta_num): ## update the value of idx in the given sequence and update its corresponding tree value
        ## update all values in the fenwick_sum that included the idx 
        ## to use low bit, the index MUST start from 1
        while idx<len(fenwick_sum):
            fenwick_sum[idx] += delta_num
            idx += self.low_bit(idx)
        return None
    
    def get_fenwick_sum(self,fenwick_sum, a,b ): ## find sum(nums[a:b+1])
        ## first get sum(nums[:b+1])
        ## then get sum(nums[:a])
        ## then diff
        
        sum_b = 0
        while b>0:
            sum_b += fenwick_sum[b]
            b -= self.low_bit(b)
            
        sum_a = 0
        a = a-1 ## as we need sum from a to b
        while a>0:
            sum_a += fenwick_sum[a]
            a -= low_bit(a)
        
        return sum_b - sum_a
    
    def low_bit(self, n):
        return (n & -n)
    
    def countSmaller(self, nums):
        ## first find unique elts in nums
        from sortedcontainers import SortedSet
        numdic = list(SortedSet(nums))
        numdic = {n:i+1 for i,n in enumerate(numdic)}
        
        ## record ranks so far, starting from very right elt of nums
        ## to use fenwick, we need the fenwick_sum idx to start from 1, so we can use low_bit()
        fenwick_sum = [0]*(len(numdic)+1)
        res = []
        for n in nums[::-1]:
            rkn = numdic[n] ## if we use ranks to keep track of current rks showed up, then we need to compute sum(ranks[:rkn])-- fenwick tree
            res.append(self.get_fenwick_sum(fenwick_sum,0,rkn-1))
            self.update_tree(fenwick_sum, rkn, 1)
        return res[::-1]
    
class Solution0:
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        ## Fenwick tree
        ## time = update O(log(n))
        ## time = query O(log(n))
        ## space=  O(n)
        """
        # import sys
        # sys.stdout = open(os.devnull, 'w')
        # this is to turn off print
        
        
        def lowbit(n): 
            ## the lowest nonzero binary bit
            ## e.g. 3 & -3 -->1; 
            ##      4 & -4 --> 4
            ## while n: bit = n & (-n), n -= bit
            ## this will go through all bits of n
            return (n & (-n) )
        
        
        
        def update(pos, value, ranking):
            # print(f"update pos: {pos}")
            if pos == 0: return 
            while pos<len(ranking):
                ## given a ranking position pos
                ## between all numbers [pos, top-1]
                ## if later, we visited a position, say P,
                ## all ranks that we visited and less than P (starting from P-1) will contribute to P's result
                ## 
                ranking[pos] += value
                pos += lowbit(pos)
            #     print(f"while pos: {pos}")
            # print(f"ranking {ranking}")
            # print()
            
        def getsum(pos, ranking):
            # print(f"pos getsum: {pos}")
            res = 0
            while pos>0:
                # print(f"while pos: {pos}")
                res += ranking[pos]
                pos -= lowbit(pos)
            # print()

            return res
            
        if not nums: return []

        

        dic = {}
        for r, k in enumerate( sorted(list(set(nums))) ):
            dic[k] = r + 1

        ranking = [0]*len(dic) + [0]
        res = []
        for n in nums[::-1]:

            pos = dic[n]
            update(pos, 1, ranking)   
            res.append(getsum(pos-1, ranking))
            
        return res[::-1]

    def countSmaller_brutal(self, nums: List[int]) -> List[int]:
        ## brutal
        N = len(nums)
        
        res = [0]*(N)
        
        for i in range(N-2,-1,-1):
            for j in range(i+1,N):
                if nums[j]<nums[i]:
                    res[i] += 1
                    
        return res
    
    def countSmaller_too_slow(self, nums: List[int]) -> List[int]:
        ## keep track of max index so far
        ## max_index[i] := the index of max value in nums[i:]
        N = len(nums)
        max_index = [-1]*N
        max_index[-1] = N-1
        max_index_set = [N-1]
        cnt_max_index = collections.defaultdict(int)
        cnt_max_index[N-1] += 1
        max_index_min_value = collections.defaultdict(int)
        max_index_min_value[N-1] = N-1
        res = [0]*N
        
        for i in range(N-2,-1,-1):
            cur_max_index = max_index[i+1]
            if nums[i] > nums[cur_max_index]:
                max_index[i] = i
                res[i] = N - i - 1
                max_index_set.append(i)
                cnt_max_index[i] += 1
                max_index_min_value[i] = nums[i]
            else:
                max_index[i] = cur_max_index
                ## search for next max
                my_cnt = 0
                for j in max_index_set:
                    if nums[i] > nums[j]:
                        my_cnt += cnt_max_index[j]
                    else:
                        if nums[i] <= max_index_min_value[j]:
                            continue
                        for k in range(j - cnt_max_index[j]+1, j):
                            if nums[i]>nums[k]:
                                my_cnt+= 1
                        
                cnt_max_index[cur_max_index] += 1
                max_index_min_value[cur_max_index] = min(max_index_min_value[cur_max_index], nums[i])
                res[i] = my_cnt

#             print(i,res[i])
#             print(max_index_set)
#             print(cnt_max_index)
#             print()
        return res