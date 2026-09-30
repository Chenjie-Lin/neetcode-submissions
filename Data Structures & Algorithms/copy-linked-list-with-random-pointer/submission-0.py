"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        address = {None: None}
        current = head
        while current:
            address[current] = Node(current.val) 
            current = current.next
            
        
        current = head
        while current:
            address[current].next = address[current.next]
            address[current].random = address[current.random]
            current = current.next

        return address[head]

