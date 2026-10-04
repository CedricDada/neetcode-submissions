# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque([root])
        res = []
        if root is None:
            return []
        while len(queue) > 0:
            next_level = []
            n = len(queue)
            for _ in range(n):
                node = queue.popleft()
                next_level.append(node.val)
                for child in [node.left, node.right]:
                    if child is not None:
                        queue.append(child)
            # on a vider tous les noeuds de ce niveau 
            res.append(next_level)
        return res