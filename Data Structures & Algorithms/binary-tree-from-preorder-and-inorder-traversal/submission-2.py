# # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# class Solution:
#     def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
#         if not preorder or not inorder:
#             return None

#         root = TreeNode(preorder[0])
#         mid = inorder.index(preorder[0])
#         root.left = self.buildTree(preorder[1 : mid + 1], inorder[:mid])
#         root.right = self.buildTree(preorder[mid + 1 :], inorder[mid + 1 :])
#         return root

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # 1. Dictionnaire pour trouver l'indice dans inorder en O(1)
        # { valeur_du_noeud : son_indice_dans_inorder }
        inorder_map = {val: idx for idx, val in enumerate(inorder)}
        
        # Pointeur qui avance dans la liste preorder au fur et à mesure
        self.pre_idx = 0

        def helper(left: int, right: int) -> Optional[TreeNode]:
            # Condition d'arrêt : s'il n'y a plus d'éléments dans cette plage
            if left > right:
                return None

            # La valeur de la racine actuelle est pointée par self.pre_idx
            root_val = preorder[self.pre_idx]
            root = TreeNode(root_val)
            
            # On avance le pointeur pour le prochain appel récursif
            self.pre_idx += 1

            # On récupère l'indice de la racine dans inorder en O(1)
            mid = inorder_map[root_val]

            # IMPORTANT : On construit TOUJOURS la gauche avant la droite
            # car preorder visite la Racine -> puis toute la Gauche -> puis la Droite
            root.left = helper(left, mid - 1)
            root.right = helper(mid + 1, right)

            return root

        # On lance la récursion sur toute la plage du tableau inorder
        return helper(0, len(inorder) - 1)