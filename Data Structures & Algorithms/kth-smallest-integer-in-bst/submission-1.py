# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # in order dfs sorts the array
        # iterative dfs:
        
        stack = []
        cur_node = root

        while cur_node or stack:
            while cur_node:
                stack.append(cur_node)
                cur_node = cur_node.left
            
            # cur_node is now null, so pop from stack
            cur_node = stack.pop()
            k -= 1

            # if kth node found, return 
            if k == 0:
                return cur_node.val
            
            # if kth node not found, visit right child
            cur_node = cur_node.right


        