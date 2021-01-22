# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> TreeNode:
        self.res = None
        self.pre = None
        def dfs(root):
            if not root:
                return
            if root.val > p.val:
                dfs(root.left)
            if self.pre:
                if self.pre.val == p.val:
                    self.res = root
                    self.pre = root
                    return
            self.pre = root
            if root.val <= p.val:
                dfs(root.right)
        dfs(root)
        return self.res