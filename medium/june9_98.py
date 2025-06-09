"""
98. Validate Binary Search Tree (Medium)

Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
 

Example 1:


Input: root = [2,1,3]
Output: true
Example 2:


Input: root = [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.
 

Constraints:

The number of nodes in the tree is in the range [1, 104].
-231 <= Node.val <= 231 - 1
"""

class TreeNode:
    def __init__(self, val = 0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root) -> bool:
        leftBound = float('-inf')
        rightBound = float('inf')

        isValid = True

        def checkNode(node, LB = leftBound, RB = rightBound, ):
            nonlocal isValid

            if isValid == True:
                if node.left is not None:
                    checkNode(node.left, LB = LB, RB = node.val, )
                
                if not LB < node.val < RB:
                    isValid = False
                    #break out of everything

                if node.right is not None:
                    checkNode(node.right, LB = node.val, RB = RB, )
        

        checkNode(root, leftBound, rightBound)
        return isValid











def buildTree(nodeValues: list[int]):

    # handle edge case with no nodes
    if not nodeValues:
        return None
    
    root = TreeNode(val = nodeValues[0])
    node_queue = [root]
    array_index = 1 # start at the position after the root
    
    while len(node_queue) > 0 and array_index < len(nodeValues):
        current_node = node_queue.pop(0)

        # try to create a left child
        if array_index < len(nodeValues) and nodeValues[array_index] is not None:
            current_node.left = TreeNode(val=nodeValues[array_index])
            node_queue.append(current_node.left)
        array_index += 1
        # try to create a right child
        if array_index < len(nodeValues) and nodeValues[array_index] is not None:
            current_node.right = TreeNode(val=nodeValues[array_index])
            node_queue.append(current_node.right)
        array_index += 1
        
    return root



case1 = [3,1,4,None,None,5,6]

tree1 = buildTree(case1)

S = Solution
answer = S.isValidBST(S, tree1)

print(answer)