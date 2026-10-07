# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head

        while True:
            if not slow or not fast or not slow.next or not fast.next or not fast.next.next:
                return False
            slow = slow.next
            fast = fast.next.next
            if slow.val == fast.val:
                return True
        return False