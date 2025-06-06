"""
Binary Tree Inorder Traversal (Easy)

Given the root of a binary tree, return the inorder traversal of its nodes' values

Example 1:

Input: root = [1,null,2,3]

Output: [1,3,2]

Example 2:

Input: root = [1,2,3,4,5,null,8,null,null,6,7,9]

Output: [4,2,6,5,7,1,3,9,8]

"""

class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right


class Solution:
     def inorderTraversal(self, root) -> list[int]:
        answer = []
        
        if not root:
            return answer
        
        def processNode(currentNode):
            if currentNode.left is not None:
                processNode(currentNode.left)
            
            answer.append(currentNode.val)

            if currentNode.right is not None:
                processNode(currentNode.right)
    
        processNode(root)
        return answer


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


test = buildTree([1,2,3,4,5,None,8,None,None,6,7,9])

s = Solution
inOrderList = s.inorderTraversal(s, test)

print(inOrderList)