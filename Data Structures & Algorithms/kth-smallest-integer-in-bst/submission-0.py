from collections import deque
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # 1. Obtenir la vraie hauteur maximale de l'arbre
        def get_height(node):
            if not node:
                return 0
            return 1 + max(get_height(node.left), get_height(node.right))
        
        h = get_height(root)
        n = (2 ** h) - 1  # Taille requise pour un arbre binaire parfait
        
        keys = [-1] * n
        
        # 2. Remplir le tableau en respectant les indices de base 0
        def dfs_fill(node, i):
            if node and i < n:
                keys[i] = node.val
                dfs_fill(node.left, 2 * i + 1)
                dfs_fill(node.right, 2 * i + 2)

        dfs_fill(root, 0)
        sorted_keys = []
        
        # 3. Le système de sauts (parcours infixe) appliqué sur le tableau
        def inorder_array(i):
            if i < n:
                inorder_array(2 * i + 1)      # Sauter au plus à gauche
                if keys[i] != -1:             # Si le nœud existe, l'ajouter
                    sorted_keys.append(keys[i])
                inorder_array(2 * i + 2)      # Prendre l'élément de droite

        inorder_array(0)
        
        return sorted_keys[k - 1]