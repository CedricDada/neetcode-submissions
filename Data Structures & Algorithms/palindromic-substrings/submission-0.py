class Solution:
    def countSubstrings(self, s: str) -> int:
        t = "#" + "#".join(s) + "#"
        nb = 0

        # On itère sur absolument tous les caractères (lettres et #)
        for i in range(len(t)):
            # On démarre les pointeurs SUR le centre
            l = i
            r = i
            
            while l >= 0 and r < len(t):
                if t[l] == t[r]:
                    # La règle d'or : si les extrémités sont des lettres, on compte.
                    if t[l] != "#":
                        nb += 1
                        
                    l -= 1
                    r += 1
                else:
                    break
                    
        return nb