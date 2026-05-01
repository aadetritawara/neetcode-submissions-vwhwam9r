# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        if not subRoot: # null is always a subtree
            return True
        if not root:    # root is null and subRoot is non null
            return False
        
        # check if current tree is the same as subRoot
        if self.areSameTree(root, subRoot):
            return True

        # otherwise check left and right children recursively
        return (
            self.isSubtree(root.left, subRoot) or 
            self.isSubtree(root.right, subRoot)
        )

    # helper function to check if two trees are the same:
    def areSameTree(self, x, y) -> bool:
        if not x and not y:
            return True
        if x and y and x.val == y.val:
            return (
                self.areSameTree(x.left, y.left) and
                self.areSameTree(x.right, y.right)
            )
        else:
            return False


