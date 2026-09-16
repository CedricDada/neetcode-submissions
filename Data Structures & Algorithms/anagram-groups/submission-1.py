class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = defaultdict(list)
        
        for word in strs:
            # Un tableau de 26 zéros pour compter les lettres (de 'a' à 'z')
            count = [0] * 26 
            for c in word:
                # ord(c) - ord('a') donne l'index de 0 à 25
                count[ord(c) - ord('a')] += 1
            
            # On convertit le tableau en tuple pour pouvoir l'utiliser comme clé
            anagram_map[tuple(count)].append(word)
            
        return list(anagram_map.values())