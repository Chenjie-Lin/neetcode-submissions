# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = 0
        dummy = ListNode(0, head)
        l1 = dummy
        l2 = dummy
        while l1:
            l1 = l1.next
            count += 1
        
        for _ in range(count - n - 1):
            l2 = l2.next
        l2.next = l2.next.next
        
        return dummy.next
        