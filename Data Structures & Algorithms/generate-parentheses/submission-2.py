class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        res = []
        
        def dfs(stack, path):
            if len(path) == 2 * n:
                res.append("".join(path))
                return
            
            if len(stack) == 0:
                path.append("(")
                stack.append("(")
                dfs(stack, path)
                path.pop()
                stack.pop()
            else:
                # Choix 1: Fermer une parenthèse (toujours possible si le stack n'est pas vide)
                path.append(")")
                stack.pop()
                dfs(stack, path)
                stack.append('(')
                path.pop()
                
                # Choix 2: Ouvrir une parenthèse (possible UNIQUEMENT si on en a moins de n)
                if path.count('(') < n:
                    path.append("(")
                    stack.append("(")
                    dfs(stack, path)
                    stack.pop()
                    path.pop()

        dfs([], [])
        return res