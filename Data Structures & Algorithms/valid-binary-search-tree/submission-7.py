# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution: # le piège ici serait de vérifier la condition juste pour chaque noeud en ignorant l'héritage des parents et des grands parents, par exemple si les petits fils d'un noeud ne vérifient pas la condition vis à vis du grand parent, on n'a pas un bst
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def valid(node, left, right):
            if not node:
                return True
            if not (left < node.val < right):
                return False

            return valid(node.left, left, node.val) and valid(
                node.right, node.val, right
            )

        return valid(root, float("-inf"), float("inf"))