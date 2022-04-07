'''
160. Intersection of Two Linked Lists
Easy

8454

842

Add to List

Share
Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect. If the two linked lists have no intersection at all, return null.

For example, the following two linked lists begin to intersect at node c1:


The test cases are generated such that there are no cycles anywhere in the entire linked structure.

Note that the linked lists must retain their original structure after the function returns.

Custom Judge:

The inputs to the judge are given as follows (your program is not given these inputs):

intersectVal - The value of the node where the intersection occurs. This is 0 if there is no intersected node.
listA - The first linked list.
listB - The second linked list.
skipA - The number of nodes to skip ahead in listA (starting from the head) to get to the intersected node.
skipB - The number of nodes to skip ahead in listB (starting from the head) to get to the intersected node.
The judge will then create the linked structure based on these inputs and pass the two heads, headA and headB to your program. If you correctly return the intersected node, then your solution will be accepted.
'''



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        lenA = 0
        node = headA
        while node:
            lenA += 1
            node = node.next
            
        lenB =0
        node = headB
        while node:
            lenB += 1
            node = node.next
        
        nodeElse = None
        dff = 0
        if lenA > lenB:
            dff = lenA - lenB
            node = headA
            nodeElse = headB
        else:
            dff = lenB - lenA
            node = headB
            nodeElse = headA
            
        while dff>0:
            dff -= 1
            node = node.next
            
        while node!=nodeElse:
            node = node.next
            nodeElse = nodeElse.next
            
        return node
                
            
    def getIntersectionNode_slow_fast(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        ## create cycle
        ## changed linked list structure!
        if headA is None or headB is None: return None
        
        slow = headA
        fast = headA
        glued = False
        while fast:
            if slow is None:
                slow = headB
            if fast.next is None and glued:
                return None
            elif fast.next is None:
                fast.next = headB
                glued = True
            fast = fast.next.next
            if slow == fast: 
                break
        fast = headA
        while fast!=slow:
            fast = fast.next
            slow = slow.next
            
        return fast
        

    def getIntersectionNode_glue(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        p1 = headA ## glue a and b together
        p2 = headB
        while p1 != p2:
            if p1 is None: p1 = headB
            else: p1 = p1.next
            if p2 is None: p2 = headA
            else: p2 = p2.next
            
        return p1
        
    def getIntersectionNode_extra_mem(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        stackA = collections.deque()
        stackB = collections.deque()
        
        while headA:
            stackA.append(headA)
            headA = headA.next
            

        while headB:
            stackB.append(headB)
            headB = headB.next
        
        res = None
        # print(stackA)
        # print(stackB)
        while stackA and stackB:
            a = stackA.pop()
            b = stackB.pop()
            # print(a)
            # print(b)
            if a!=b:
                return res
            
            res = a
            
        return res
            
            