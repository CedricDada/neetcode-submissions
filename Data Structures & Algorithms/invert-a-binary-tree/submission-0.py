# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        #implémentons un parcourt en profondeur 
        def dfs(root : Optional[TreeNode]):
            if root == None:
                return
            tmp = root.left
            root.left = root.right
            root.right = tmp

            if root.left:
                dfs(root.left)
            if root.right:
                dfs(root.right)
        
        dfs(root)
        return root
