# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:


        def dfs(curr, p, q):

            if curr.val == p.val or curr.val == q.val:
                return curr

            if p.val < curr.val and q.val < curr.val:
                return dfs(curr.left, p, q)
            elif p.val > curr.val and q.val > curr.val:
                return dfs(curr.right, p, q)
            else:
                return curr

        return(dfs(root,p,q))

        