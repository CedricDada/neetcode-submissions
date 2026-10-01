# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        res = dummy
        ret = 0
        while l1 and l2:
            sum = l1.val + l2.val + ret
            # la retenue a déjà été consommée
            ret = 0
            if sum > 9:
                ret += 1
                sum = sum - 10
            
            next = ListNode(sum, None)
            dummy.next = next
            l1 = l1.next
            l2 = l2.next
            dummy = dummy.next
        while l1:
            sum = l1.val + ret
            ret = 0
            if sum > 9:
                ret += 1
                sum = sum - 10
            next = ListNode(sum, None)
            dummy.next = next
            l1 = l1.next
            dummy = dummy.next
        
        while l2:
            sum = l2.val + ret
            ret = 0
            if sum > 9:
                ret += 1
                sum = sum - 10
            next = ListNode(sum, None)
            dummy.next = next
            l2 = l2.next
            dummy = dummy.next
        
        if ret > 0:
            next = ListNode(ret, None)
            dummy.next = next
        return res.next


