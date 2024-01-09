# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        
        base1 = []
        base2 = []
        def traverse(node, base):
            if not (node.left or node.right):
                base.append(node.val)
            if node.left:
                traverse(node.left, base)
            if node.right:
                traverse(node.right, base)
        traverse(root1, base1)
        traverse(root2, base2)
        return base1 == base2
        

# intuition, traverse tree, then check if it's root node, if so, then add to a nonlocal list
# a node is root, if left and right are both None
# by passing in a defined list, it can modify the value and retain modification when recursion is completed
# then check if the 2 list are equal