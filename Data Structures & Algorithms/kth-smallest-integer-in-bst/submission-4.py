# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # res = None
        # count = 0

        # def dfs(curr):
        #     nonlocal res
        #     nonlocal count
        #     if curr:

        #         dfs(curr.left)
        #         count += 1
        #         if count == k:
        #             res = curr.val
        #             return
        #         dfs(curr.right)

            

        # dfs(root)
        # return res

        n = 0
        stack = []
        curr = root

        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left

            curr = stack.pop()
            n += 1
            if n == k:
                return curr.val
            curr = curr.right
        
