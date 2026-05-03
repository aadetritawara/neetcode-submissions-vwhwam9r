# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # bfs
        res = []
        q = deque()
        q.append(root)

        while q:
            subres = []
            # traverse nodes at the same level
            for i in range(len(q)): 
                cur_node = q.popleft()
                if not cur_node:
                    return res
                subres.append(cur_node.val)

                # add children to queue
                if cur_node.left:
                    q.append(cur_node.left)
                if cur_node.right:
                    q.append(cur_node.right)
            res.append(subres)
        return res