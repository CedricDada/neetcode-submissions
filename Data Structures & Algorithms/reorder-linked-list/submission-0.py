from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        # 1. Calculer la longueur (ta première étape)
        length = 0
        it = head
        while it:
            length += 1
            it = it.next

        # 2. Trouver le milieu pour couper la liste en deux
        it = head
        # On avance jusqu'à la fin de la première moitié
        for _ in range((length - 1) // 2):
            it = it.next
        
        # 'it' est le dernier noeud de la 1ère moitié.
        # On sauvegarde le début de la 2ème moitié et on coupe le lien.
        second_half = it.next
        it.next = None 

        # 3. Inverser la deuxième liste (ton idée d'avoir 6--5--4)
        prev = None
        curr = second_half
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        
        # 'prev' pointe maintenant sur la nouvelle tête de la 2ème liste inversée (le '6')

        # 4. Fusionner les deux listes en alternance
        first = head
        second = prev
        
        while second:
            # Sauvegarder les noeuds suivants
            tmp1 = first.next
            tmp2 = second.next
            
            # Relier le noeud de la liste 1 au noeud de la liste 2
            first.next = second
            # Relier le noeud de la liste 2 au noeud SUIVANT de la liste 1
            second.next = tmp1
            
            # Avancer les pointeurs pour la prochaine itération
            first = tmp1
            second = tmp2