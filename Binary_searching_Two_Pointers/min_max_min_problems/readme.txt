IDEA:
1. min(max over lambda) := find the min of a set of max; where max run over a constraint
    we can: give upper bound and lower it each time

2. max(min over lambda) := find the max of a set of min; where min run over a constraint
    we can: give lower bound and increase it each time


examples:
min(max over lambda)
410. Split Array Largest Sum
Given nums which consists of integers (>=0) and an integer m (>=1), 
you can split nums into m non-empty continuous subarrays.
Now, minimize the largest sum among these m subarrays.

We want to try lower bound of (largest sum among these m subarrays):
    1. we can give posisble lower bound each time ; try to LOWER it
    2. binary search: [l, r) (right is open!, return left)
    3. l = max(nums) ## one subarray must contain the max;
    4. r = sum(nums) + 1 ## right is open, so we must +1;
    5. code structure to return l:
            while l< r:
                mid = l + (r-l)//2
                ##if update l: l = mid + 1!!!
                ##if update r: r = mid 
                tmp_sum = 0
                cnt = 0
                for t in nums:
                    if tmp_sum + t >mid:
                        cnt += 1
                        tmp_sum = t
                    else:
                        tmp_sum += t
                cnt += 1
                if cnt > m: ##each subsum is too small
                    l = mid+1
                elif cnt < m: ## each subsum is too big, we can lower it
                    r = mid - 1
                elif cnt == m: ## we maybe able to lower the subsum
                    r = mid 
                    ## what to update under "cnt == m" is very important!! 
                    ## if we take r=mid; then this BST must use [l, r), l=mid+1, r=mid to return l
                    ## if we take l=mid; then this BST must use (l, r], l=mid, r=mid-1 to return r


max(min over lambda)

Change 410. Split Array Largest Sum: to the following
Given nums which consists of integers (>=0) and an integer m (>=1), 
you can split nums into m non-empty continuous subarrays.
Now, max the smallest sum among these m subarrays.

We want to try upper bound of (smallest sum among these m subarrays):
    potential code:
    1. we can give posisble upper bound each time ; try to increase it
    2. binary search?? [l, r] -- to determine l open or r open
    3. l = min(nums) ## one subarray must contain the min;
    4. r = sum(nums) ## max possible sum;
    ## NOTE: here we haven't decided [l, r) or (l,r]
    5. code structure to return l or r??
            while l< r:
                mid = l + (r-l)//2 ## as possible smallest sum
                tmp_sum = 0
                cnt = 0
                for t in nums:
                    tmp_sum += t 
                    if tmp_sum>mid:
                        cnt += 1
                        tmp_sum = 0

                if cnt > m: ## we can increase subsum lower bound
                    l = mid+1
                elif cnt < m: ## each subsum is too big, we can lower it
                    r = mid - 1
                elif cnt == m: ## Since we are searching for upper bound different from before
                               ## we want to potentially the bound!! so
                    l = mid  ## so we MUST return r

    potential code UPDATE: after figuring out we need to return right!
    binary search (l, r] 
    l = min(nums)-1 ## one subarray must contain the min and don't reach left
    r = sum(nums) ## max possible sum;
    ## NOTE: here we haven decided (l,r]
    5. code structure to return l or r??
            while l< r:
                mid = l + (r-l)//2 ## as possible smallest sum
                tmp_sum = 0
                cnt = 0
                for t in nums:
                    tmp_sum += t 
                    if tmp_sum>mid:
                        cnt += 1
                        tmp_sum = 0

                if cnt > m: ## we can increase subsum lower bound
                    l = mid + 1
                elif cnt < m: ## each subsum is too big, we can lower it
                    r = mid - 1
                elif cnt == m: ## Since we are searching for upper bound different from before
                               ## we want to potentially the bound!! so
                    l = mid  ## so we MUST return r
            return r

    

    