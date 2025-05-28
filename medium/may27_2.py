"""
Add Two Numbers

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
        l1_current = l1
        l2_current = l2

        ans_current = ListNode()
        ans_head = ans_current
        carry = 0

        while l1_current or l2_current or carry == 1:
            val1 = l1_current.val if l1_current else 0
            val2 = l2_current.val if l2_current else 0
            ans_current.val = (val1 + val2 + carry) % 10
            if val1 + val2 + carry > 9:
                carry = 1
            else:
                carry = 0

            if l1_current:
                l1_current = l1_current.next
            if l2_current:
                l2_current = l2_current.next
            
            if l1_current or l2_current or carry:
                ans_next = ListNode()
                ans_current.next = ans_next
                ans_current = ans_current.next

        return ans_head


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
    list = []
    current = head

    while current:
        list.append(current.val)
        current = current.next

    return list

# print a linked list in a readable format
def print_linked_list(head):
    current = head

    while current:
        print(f"Node value: {current.val}")
        current = current.next



def main():
    l1 = create_linked_list([9,9,9,9,9,9,9])
    l2 = create_linked_list([9,9,9,9])
    

    s = Solution()
    sum = s.addTwoNumbers(l1, l2)
    print_linked_list(sum)

main()

"""

l1 = [2,4,3,6,8,4,3]

head = create_linked_list(l1)
print_linked_list(head)

node_list = linked_list_to_list(head)
print(node_list)
"""