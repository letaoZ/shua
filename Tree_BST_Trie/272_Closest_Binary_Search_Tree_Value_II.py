'''
272. Closest Binary Search Tree Value II
Hard

1021

33

Add to List

Share
Given the root of a binary search tree, a target value, and an integer k, return the k values in the BST that are closest to the target. You may return the answer in any order.

You are guaranteed to have only one unique set of k values in the BST that are closest to the target.

 

Example 1:


Input: root = [4,2,5,1,3], target = 3.714286, k = 2
Output: [4,3]
Example 2:

Input: root = [1], target = 0.000000, k = 1
Output: [1]
 

Constraints:

The number of nodes in the tree is n.
1 <= k <= n <= 104.
0 <= Node.val <= 109
-109 <= target <= 109
 

Follow up: Assume that the BST is balanced. Could you solve it in less than O(n) runtime (where n = total nodes)?
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestKValues(self, root: Optional[TreeNode], target: float, k: int) -> List[int]:
        
        q = collections.deque()
        def searching(q, node, target,k):
            if node is None: return
            ## this is in order traversal--> nodes are ordered naturally!!
            searching(q, node.left, target, k)
            if (len(q) < k):
                q.append(node.val)
            else:
                if abs(q[0] - target) > abs(node.val - target):
                    q.popleft()
                    q.append(node.val)
                else:
                    return
            searching(q,node.right,target,k)
        searching(q,root,target,k)
        return list(q)
    
    def closestKValues_heap(self, root: Optional[TreeNode], target: float, k: int) -> List[int]:
        ## find all pairs of diff
        
        pairs = []
        
        def search(node, pairs, target,k):
            if node is None:
                return 
            ## max heap, remove the featurest each time
            heapq.heappush(pairs, (-abs(node.val - target),node.val) )
            while len(pairs)>k:
                heapq.heappop(pairs)

            search(node.left, pairs, target, k)
            search(node.right, pairs, target, k)
        search(root, pairs, target, k)
        res = [t for _,t in pairs[:k]]
        return res
    
    def closestKValues_sort(self, root: Optional[TreeNode], target: float, k: int) -> List[int]:
        ## find all pairs of diff
        
        pairs = []
        
        def search(node, pairs, target,k):
            if node is None:
                return 
            bisect.insort(pairs, (abs(node.val - target),node.val) )
            while len(pairs)>k:
                pairs.pop()


            search(node.left, pairs, target, k)
            search(node.right, pairs, target, k)
        search(root, pairs, target, k)
        res = [t for _,t in pairs[:k]]
        return res
    
    def closestKValues_sec_pre(self, root: Optional[TreeNode], target: float, k: int) -> List[int]:
        ## find all pairs of diff
        '''
        下面的这种方法用了两个栈，pre 和 suc，其中 pre 存小于目标值的数，suc 存大于目标值的数，
        开始初始化 pre 和 suc 的时候，要分别将最接近目标值的稍小值和稍大值压入 pre 和 suc，
        然后循环k次，每次比较 pre 和 suc 的栈顶元素，看谁更接近目标值，将
        其存入结果 res 中，然后更新取出元素的栈，依次类推直至取完k个数返回即可
        time complexity: k + logn
        '''

        def addpre(pre):
            top = pre[-1]
            pre.pop()
            if top.left:
                pre.append(top.left)
                while(pre[-1].right):
                    pre.append(pre[-1].right)

        def addsuc(suc):
            top = suc[-1]
            suc.pop()
            print(top)
            if top.right:
                suc.append(top.right)
                while(suc[-1].left):
                    suc.append(suc[-1].left)


        pre, suc = collections.deque(), collections.deque() ## stacks
        
        while(root):
            if root.val <= target:
                pre.append(root)
                root = root.right
            else:
                suc.append(root)
                root = root.left
        res = []
        while(len(res)<k):
            if (len(pre) >0 and len(suc)>0):
                if (abs(pre[-1].val - target) >= abs(suc[-1].val-target)):
                    res.append(suc[-1].val)
                    if len(res) == k: return res
                    addsuc(suc)
                else:
                    res.append(pre[-1].val)
                    if len(res) == k: return res
                    addpre(pre)
            elif (len(pre) > 0):
                res.append(pre[-1].val)
                if len(res) == k: return res
                addpre(pre)
            elif (len(suc) > 0):
                res.append(suc[-1].val)
                if len(suc) == k: return res
                addsuc(suc)
            else:
                break
    
        return res
    

