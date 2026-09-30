# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0

        def dfs(curr, mVal):
            nonlocal res
            if curr:
            
                if curr.val >= mVal:
                    res += 1
                
                mVal = max(mVal, curr.val)
            
                dfs(curr.left, mVal)
                dfs(curr.right, mVal)

        dfs(root, root.val)
        return res