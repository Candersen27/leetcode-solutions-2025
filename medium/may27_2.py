"""
Add Two Numbers
(No LLMs)

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example 1:

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.


Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]


Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]

Constraints:

The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.
"""

class ListNode:
    def __init__(self, val = 0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1, l2) -> ListNode:
        pass


# helper functions to transform lists to linked lists and back.
def create_linked_list(arr):

    n = len(arr)
    current_node = None
    head = ListNode(arr[0], None)
    next_node = head
    for i in range(1, n):
        current_node = next_node
        next_node = ListNode(arr[i], None)
        current_node.next = next_node
    # return the head of the linked list
    return head

def linked_list_to_list(head):
    pass

# print a linked list in a readable format
def print_linked_list(head):
    current = head
    next = current.next

    while current:
        print(f"Node value: {current.val}")
        current = current.next


"""
def main():
    l1 = create_linked_list([2,4,3])
    l2 = create_linked_list([5,6,4])


    s = Solution
    s.addTwoNumbers
"""

l1 = [2,4,3,6,8,4,3]

head = create_linked_list(l1)
print_linked_list(head)