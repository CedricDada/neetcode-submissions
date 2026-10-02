# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        #implémentons un parcours en largeur 
        depth = 0
        if root == None:
            return depth

        queue = deque([root])

        while queue:

            #on doit vider tous les noeuds du niveau actuel et ajouter les enfants
            len_level = len(queue)
            for _ in range(len_level):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            depth += 1
        return depth
            
            

        