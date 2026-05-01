# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # iterative dfs using stack
        stack = [[root, 1]]
        max_depth = 0

        while stack:
            node, depth = stack.pop()

            if node:
                max_depth = max(max_depth, depth)
                # add children of current node to the stack
                stack.append([node.left, depth + 1])
                stack.append([node.right, depth + 1])
        return max_depth


        