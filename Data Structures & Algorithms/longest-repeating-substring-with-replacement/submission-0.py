class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        count = collections.defaultdict(int)
        max_f = 0
        res = 0
        for r in range(len(s)):
            count[s[r]] += 1

            max_f = max(max_f, count[s[r]]) #vu que j'ai modifié count[s[r]] c'est seulement lui qui peut actuellement etre supérieur à max_f

            if r-l+1 - max_f > k: # pour avoir une fenetre valide , il faut que taille de la fenetre - la fréquence du caractère le plus présent soit <= k 
                count[s[l]] -= 1
                l+=1

            # c'est après c'etre rassurer que le segment [l,r] est bien valide qu'on mets à jour 
            res = max(res, r-l+1)
        return res
