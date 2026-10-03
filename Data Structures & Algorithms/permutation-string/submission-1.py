class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        # Tableaux fixes de taille 26 (beaucoup plus rapide qu'un dict)
        s1_count = [0] * 26
        window_count = [0] * 26

        # Initialisation de la première fenêtre
        for i in range(len(s1)):
            s1_count[ord(s1[i]) - ord('a')] += 1
            window_count[ord(s2[i]) - ord('a')] += 1

        # Comparaison des tableaux (O(26) -> O(1))
        if s1_count == window_count:
            return True

        # Glissement de la fenêtre
        l = 0
        for r in range(len(s1), len(s2)):
            # On ajoute la nouvelle lettre à droite
            window_count[ord(s2[r]) - ord('a')] += 1
            
            # On retire la lettre qui sort à gauche
            window_count[ord(s2[l]) - ord('a')] -= 1
            l += 1

            if s1_count == window_count:
                return True

        return False