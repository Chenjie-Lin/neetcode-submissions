# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []

        q = collections.deque()
        q.append(root)

        while q:
            qLen = len(q)
            level = []
            for _ in range(qLen):
                node = q.popleft()
                level.append(node.val) if node else None
                q.append(node.left) if node else None
                q.append(node.right) if node else None
            if level:
                res.append(level)
        return res



