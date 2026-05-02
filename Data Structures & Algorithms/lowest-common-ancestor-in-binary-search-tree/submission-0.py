# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        cur = root

        while cur:
            if p.val < cur.val and q.val < cur.val:
                # search left subtree
                cur = cur.left
            elif p.val > cur.val and q.val > cur.val:
                # search right subtree
                cur = cur.right
            else:
                # either a split occurs (p & q in separate subtrees)
                # or one of p/q is the current node
                return cur