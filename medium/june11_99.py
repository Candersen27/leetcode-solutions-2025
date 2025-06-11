"""
Recover Binary Search Tree (medium)

You are given the root of a binary search tree (BST), where the values of exactly two nodes of the tree were swapped by mistake. Recover the tree without changing its structure.

Input: root = [1,3,null,null,2]
Output: [3,1,null,null,2]
Explanation: 3 cannot be a left child of 1 because 3 > 1. Swapping 1 and 3 makes the BST valid.

Input: root = [3,1,4,null,null,2]
Output: [2,1,4,null,null,3]
Explanation: 2 cannot be in the right subtree of 3 because 2 < 3. Swapping 2 and 3 makes the BST valid.

Constraints:

The number of nodes in the tree is in the range [2, 1000].
-2^31 <= Node.val <= 2^31 - 1
 
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def recoverTree(self, root) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        nodeValues = []
        firstViolation = None
        secondViolation = None
        potentialSecondViolation = None

        def recordNode(node) -> list:
            nonlocal nodeValues
            if node.left is not None: # left
                recordNode(node.left)
            
            nodeValues.append((node, node.val)) # self

            if node.right is not None: # right
                recordNode(node.right)

        def swapNodeVals(node1, node2):
            temp = node1.val
            node1.val = node2.val
            node2.val = temp

        recordNode(root)

        for i in range(len(nodeValues) - 1):
            if nodeValues[i][1] > nodeValues[i + 1][1]:
                if firstViolation is None:
                    firstViolation = nodeValues[i][0]
                    potentialSecondViolation = nodeValues[i + 1][0]

                else:
                    secondViolation = nodeValues[i + 1][0]
                    swapNodeVals(firstViolation, secondViolation)
                    break
        
        if secondViolation is None:
            swapNodeVals(firstViolation, potentialSecondViolation)

def buildTree(nodeValues: list):
    # handle edge case with no nodes
    if not nodeValues or nodeValues[0] is None:
        return None
    
    root = TreeNode(val=nodeValues[0])
    node_queue = [root]
    array_index = 1  # start at the position after the root
    
    while len(node_queue) > 0 and array_index < len(nodeValues):
        current_node = node_queue.pop(0)

        # try to create a left child
        if array_index < len(nodeValues):
            if nodeValues[array_index] is not None:
                current_node.left = TreeNode(val=nodeValues[array_index])
                node_queue.append(current_node.left)
            array_index += 1
            
        # try to create a right child
        if array_index < len(nodeValues):
            if nodeValues[array_index] is not None:
                current_node.right = TreeNode(val=nodeValues[array_index])
                node_queue.append(current_node.right)
            array_index += 1
        
    return root

def printTreeStructure(node, level=0, prefix="Root: "):
    if node is not None:
        print(" " * (level * 4) + prefix + str(node.val))
        if node.left is not None or node.right is not None:
            printTreeStructure(node.left, level + 1, "L--- ")
            printTreeStructure(node.right, level + 1, "R--- ")


def testCase(array):
    
    def getInOrder(node):
        result = []
        if node:
            result.extend(getInOrder(node.left))
            result.append(node.val)
            result.extend(getInOrder(node.right))
        return result
    
    root = buildTree(array)
    print("Tree structure:")
    printTreeStructure(root)
    print("Before:", getInOrder(root))
    
    S = Solution()
    S.recoverTree(root)
    
    print("After:", getInOrder(root))
    return getInOrder(root)


testCases = [[1, 3, None, None, 2], [3, 1, 4, None, None, 2], [6, 2, 7, 1, 3, 5, 8]]

for case in testCases:
    testCase(case)