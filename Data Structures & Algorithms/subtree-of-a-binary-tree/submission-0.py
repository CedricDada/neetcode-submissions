from collections import deque
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # Fonction pour vérifier si deux arbres sont strictement identiques
        def isSameTree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
            if not p and not q:
                return True
            if not p or not q:  # Si l'un est nul mais pas l'autre
                return False
            if p.val != q.val:  # Si les valeurs diffèrent
                return False
            # On continue la vérification sur les enfants gauches ET droits
            return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)

        if not subRoot:
            return True
        if not root:
            return False

        queue = deque([root])

        while queue:
            node = queue.popleft()
            
            # On s'assure que le nœud dépilé n'est pas None
            if node:
                if node.val == subRoot.val:
                    if isSameTree(node, subRoot):
                        return True
                
                # On ajoute les enfants s'ils existent
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                    
        return False