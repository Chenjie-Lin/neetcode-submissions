# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        def dfs(a,b):
            if not a and not b:
                return True
            
            if not a or not b:
                return False

            same = dfs(a.left,b.left) and dfs(a.right,b.right)

            if a.val != b.val:
                return False
            
            return same
        
        return dfs(p,q)
            