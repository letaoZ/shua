'''
19. Remove Nth Node From End of List
Medium

9485

448

Add to List

Share
Given the head of a linked list, remove the nth node from the end of the list and return its head.

 

Example 1:


Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
Example 2:

Input: head = [1], n = 1
Output: []
Example 3:

Input: head = [1,2], n = 1
Output: [1]
 

Constraints:

The number of nodes in the list is sz.
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        p1 = head
        
        while p1 and n:
            p1 = p1.next
            n -= 1
        if n > 0:
            return head
        if p1 is None:
            return head.next
        
        p2 = head
        pre = None
        while p1:
            p1 = p1.next
            pre = p2
            p2 = p2.next
            
        pre.next = p2.next
        return head