# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def traverse(node):
            nonlocal total
            if not node:
                return 0
            if low <= node.val <= high:
                total += node.val
            if node.val > low:
                traverse(node.left)
            if node.val < high:
                traverse(node.right)
        total = 0
        traverse(root)
        return total

# binary tree search
# recursively, first check if node is valid
# then check if in range, if in range then add to total
# then check if more than low or less than high individually
# then more left and right respectively until reaching the edge