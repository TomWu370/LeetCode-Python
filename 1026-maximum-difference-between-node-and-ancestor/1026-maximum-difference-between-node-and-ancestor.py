# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def dfs(path, maxVal, node):
            path.append(node.val)

            if node.left:
                maxVal = dfs(path, maxVal, node.left)
            if node.right:
                maxVal = dfs(path, maxVal, node.right)
            if not (node.left or node.right):
                maxVal = max(maxVal, max(path)-min(path))

            path.pop()
            return maxVal
        return dfs([], 0, root)

# intuition, using depth first search, for each path, store the ancestor node, then for each end node, calculate the difference
# then do the right right as well
# after all sides are done, go to the next ancestor node
# to begin, at the start of iteration, the current node is always appended to a list
# then it will continue traversing left or right until the end is reached
# then a calculation is done, by adjusting the current max difference by subtracting the largest from the smallest item in list
# then after that node is used in calculationg, it is removed from list
# the 2 declaration of maxVal works because the current best maxVal is returned in the end, so there is no bad overwriting
# case 2 has a weird binary tree therefore max and min works, because the tree is 1 path, therefore when it reaches the end
# the list will have all the nodes inside the list