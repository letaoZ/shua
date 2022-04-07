'''

23. Merge k Sorted Lists
Hard

11715

458

Add to List

Share
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

 

Example 1:

Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6
Example 2:

Input: lists = []
Output: []
Example 3:

Input: lists = [[]]
Output: []
 

Constraints:

k == lists.length
0 <= k <= 104
0 <= lists[i].length <= 500
-104 <= lists[i][j] <= 104
lists[i] is sorted in ascending order.
The sum of lists[i].length will not exceed 104.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    
        setattr(ListNode, "__lt__", lambda x,y: x.val<=y.val) ## min heap
        
        minheap = []
        dummy = ListNode()
        res = dummy
        for node in lists:
            if node:
                heapq.heappush(minheap, (node.val, node))
            
        # print(minheap)
        while minheap:
            v, node = heapq.heappop(minheap)
            res.next = node
            res = res.next
            if node.next:
                heapq.heappush(minheap, (node.next.val, node.next))
        return dummy.next

# class Solution:
#     def mergeKLists(self, lists: List[ListNode]) -> ListNode:
#         h = [(head.val, idx, head) for idx, head in enumerate(lists) if head is not None]
#         heapq.heapify(h)
#         dummy = ListNode()
#         last = dummy
#         while h:
#             val, idx, node = heapq.heappop(h)
#             last.next, last = node, node
#             if last.next is not None:
#                 heapq.heappush(h, (last.next.val, idx, last.next))
#         return dummy.next