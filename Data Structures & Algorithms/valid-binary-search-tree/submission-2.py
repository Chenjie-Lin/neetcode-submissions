# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(curr, low, high):
            if not curr:
                return True

            if not (low < curr.val < high):
                return False

            res = dfs(curr.left, low, curr.val) and dfs(curr.right, curr.val, high)

            return res
            


        return dfs(root, float("-infinity"), float("infinity"))