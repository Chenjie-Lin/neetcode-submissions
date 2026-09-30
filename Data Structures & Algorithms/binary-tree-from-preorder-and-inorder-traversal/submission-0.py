# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        hashset = {}
        for i, x in enumerate(inorder):
            hashset[x] = i
        
        pre = 0

        def dfs(l,r):
            nonlocal pre

            if l > r:
                return None

            curr = TreeNode(preorder[pre])
            pre += 1
            mid = hashset[curr.val]

            curr.left = dfs(l, mid - 1)
            curr.right = dfs(mid + 1, r)

            return curr
        

        return dfs(0, len(inorder) - 1)