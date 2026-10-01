# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_sum = float('-inf')

        def dfs(curr):
            if not curr:
                return 0
            nonlocal max_sum
            left = max(dfs(curr.left),0)
            right = max(dfs(curr.right),0)
            total = curr.val + left + right
            max_sum = max(total, max_sum)

            return curr.val + max(left,right)

        dfs(root)
        return max_sum
            