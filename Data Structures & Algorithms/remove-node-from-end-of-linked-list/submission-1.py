# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        tmp = head

        # déterminons la longueur de la liste 
        length = 0

        while tmp:
            length += 1
            tmp = tmp.next
        
        if length == 1:
            return None

        new_head = ListNode()
        new_head.next = head
        tmp = new_head

        # nous voulons retirer l'élément length - n + 1

        for _ in range(length - n):
            print(tmp.val)
            tmp = tmp.next
        
        tmp.next = tmp.next.next

        return new_head.next