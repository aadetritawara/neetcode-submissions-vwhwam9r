# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # bfs processes one tree level at a time using a queue
        # count levels traversed until queue is empty
        levels = 0
        q = deque()

        if root:
            q.append(root)
        
        while q:
            # find and process all nodes at the same level
            for i in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            levels += 1
        return levels




        