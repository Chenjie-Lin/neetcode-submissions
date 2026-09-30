# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        if not head:
            return
        dummy = ListNode(0, head)
        group = dummy

        while True:
            
            fast = group

            for _ in range(k):

                fast = fast.next

                if not fast:
                    return dummy.next

            nxt = fast.next

            prev = nxt
            current = group.next
            while current != nxt:
                n = current.next
                current.next = prev
                prev = current
                current = n

            tmp = group.next
            group.next = fast
            group = tmp
            

                

                

