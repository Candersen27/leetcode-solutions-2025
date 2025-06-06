"""
141. Linked List Cycle
Easy (no LLMs)

Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.

"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        
        if head == None:
            return False
        
        nodeSlow = head
        nodeFast = head

         
        while True:

            
            
            if nodeFast.next is not None and nodeFast.next.next is not None:
                nodeFast = nodeFast.next.next
                nodeSlow = nodeSlow.next
            else:
                return False

            if nodeFast == nodeSlow:
                return True

            

        
        
        return True


LN = ListNode(12)

print(LN)