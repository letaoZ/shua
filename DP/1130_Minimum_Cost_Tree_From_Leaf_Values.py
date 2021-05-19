
'''
1130. Minimum Cost Tree From Leaf Values
Medium
Given an array arr of positive integers, consider all binary trees such that:

Each node has either 0 or 2 children;
The values of arr correspond to the values of each leaf in an in-order traversal of the tree.  (Recall that a node is a leaf if and only if it has 0 children.)
The value of each non-leaf node is equal to the product of the largest leaf value in its left and right subtree respectively.
Among all possible binary trees considered, return the smallest possible sum of the values of each non-leaf node.  It is guaranteed this sum fits into a 32-bit integer.

Example 1:

Input: arr = [6,2,4]
Output: 32
Explanation:
There are two possible trees.  The first has non-leaf node sum 36, and the second has non-leaf node sum 32.

    24            24
   /  \          /  \
  12   4        6    8
 /  \               / \
6    2             2   4
 

Constraints:

2 <= arr.length <= 40
1 <= arr[i] <= 15
It is guaranteed that the answer fits into a 32-bit signed integer (ie. it is less than 2^31).

'''


class Solution:

    def mctFromLeafValues(self, arr: List[int]) -> int:
        '''
        Intuition
        Let's review the problem again.

        When we build a node in the tree, we compared the two numbers a and b.
        In this process,
        the smaller one is removed and we won't use it anymore,
        and the bigger one actually stays.

        The problem can translated as following:
        Given an array A, choose two neighbors in the array a and b,
        we can remove the smaller one min(a,b) and the cost is a * b.
        What is the minimum cost to remove the whole array until only one left?

        To remove a number a, it needs a cost a * b, where b >= a.
        So a has to be removed by a bigger number.
        We want minimize this cost, so we need to minimize b.

        b has two candidates, the first bigger number on the left,
        the first bigger number on the right.

        The cost to remove a is a * min(left, right).
        
        '''
        
        sz = len(arr)
        i = 0
        res = 0
        ## bound is ONE, because we don't need node's value
        while( len(arr)>1):
            min_a = min(arr)
            ## can also use heap
    
            idx = arr.index(min_a)
            res += min(arr[idx-1:idx]+ arr[idx+1:idx+2]) * min_a
            arr.pop(idx)
        return res
    
    
    def mctFromLeafValues_version1_bottomup_dp_save_max(self, arr: List[int]) -> int:

        ## extra space for max value between arr[i] and arr[j]
        sz = len(arr)
        pmax = [[0]*(sz) for _ in range(sz)]
        
        for i in range(sz):
            b = arr[i]
            for j in range(i,sz):
                b = max(b, arr[j])
                pmax[i][j] = b
        
        ## dp[i][j] smallest sum you can get from i to j inclusive
        sz = len(arr)
        
        dp  =[ [float('inf')]*(sz) for _ in range(sz) ]
        for k in range(sz):
            dp[k][k] = arr[k]

        for L in range(1,sz):
            for i in range(sz-L):
                j = i+L
                for k in range(i,j):
                    dp[i][j] = min(dp[i][j], pmax[i][k]*pmax[k+1][j]+ dp[k+1][j] + dp[i][k])
                    
        res = dp[0][sz-1] - sum(arr)
        return res
        
        
        
    def mctFromLeafValues_version2_topdown_dp_save_max(self, arr: List[int]) -> int:

        ## extra space for max value between arr[i] and arr[j]
        sz = len(arr)
        pmax = [[0]*(sz) for _ in range(sz)]
        
        for i in range(sz):
            b = arr[i]
            for j in range(i,sz):
                b = max(b, arr[j])
                pmax[i][j] = b
        
        ## dp[i][j] smallest sum you can get from i to j inclusive
        sz = len(arr)
        
        dp  =[ [float('inf')]*(sz) for _ in range(sz) ]
        for k in range(sz):
            dp[k][k] = arr[k]
        def searching(arr,i,j):
            # if i>j:
            #     return 0
            if dp[i][j] < float('inf'):
                return dp[i][j]
            
            
            
            ## k is where to cut
            psum = float('inf')
            for k in range(i,j):
                p = (pmax[i][k])*pmax[k+1][j]
                # p =  max(arr[i:k+1])*max(arr[k+1:j+1])
                psum = min(psum, p + searching(arr,i,k) + searching(arr,k+1,j))
            dp[i][j] = psum
            return psum
        
        res = searching(arr, 0,sz-1)
        sum_nodes = sum(arr)
        res -= sum_nodes
        return res
        
    def mctFromLeafValues_version1_topdown_dp(self, arr: List[int]) -> int:

        
        ## dp[i][j] smallest sum you can get from i to j inclusive
        sz = len(arr)
        
        dp  =[ [float('inf')]*(sz) for _ in range(sz) ]
        for k in range(sz):
            dp[k][k] = arr[k]
        def searching(arr,i,j):
            # if i>j:
            #     return 0
            if dp[i][j] < float('inf'):
                return dp[i][j]
            
            
            
            ## k is where to cut
            psum = float('inf')
            for k in range(i,j):
                
                p =  max(arr[i:k+1])*max(arr[k+1:j+1])
                psum = min(psum, p + searching(arr,i,k) + searching(arr,k+1,j))
            dp[i][j] = psum
            return psum
        
        res = searching(arr, 0,sz-1)
        sum_nodes = sum(arr)
        res -= sum_nodes
        return res