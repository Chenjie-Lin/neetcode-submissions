# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        dummy = ListNode()
        slow = head
        fast = head.next
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        l2 = slow.next
        prev = slow.next = None
        while l2:
            temp = l2.next
            l2.next = prev
            prev = l2
            l2 = temp
        
        l1, l2 = head, prev
        while l2:
            temp1, temp2 = l1.next, l2.next
            l1.next = l2
            l2.next = temp1
            l1 = temp1
            l2 = temp2
        

