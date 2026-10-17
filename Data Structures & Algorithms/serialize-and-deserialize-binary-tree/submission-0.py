class Codec:

    def serialize(self, root: Optional[TreeNode]) -> str:
        res = [] # Déclaré EN DEHORS de la fonction récursive

        def pre_order(node):
            if not node:
                res.append("N") # On marque explicitement les vides !
                return
            
            res.append(str(node.val)) # Converti en texte pour le .join()
            pre_order(node.left)
            pre_order(node.right)

        pre_order(root)
        return ",".join(res)

    def deserialize(self, data: str) -> Optional[TreeNode]:
        vals = data.split(",")
        self.i = 0 # Pointeur qui avance dans la liste vals

        def construct_tree():
            # Si on tombe sur "N", c'est une feuille vide : on s'arrête
            if vals[self.i] == "N":
                self.i += 1
                return None
            
            # Sinon, on crée le nœud en convertissant le texte en entier
            node = TreeNode(int(vals[self.i]))
            self.i += 1
            
            # Comme on a sérialisé en Preorder (Racine -> Gauche -> Droite),
            # on reconstruit exactement dans le même ordre !
            node.left = construct_tree()
            node.right = construct_tree()
            return node

        return construct_tree()