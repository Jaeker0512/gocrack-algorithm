# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.res = 0
    def pathSum(self, root: TreeNode, sum: int) -> int:
        def dfs_inner(root, sum):
            if not root:
                return
            if sum == root.val:
                self.res += 1
            dfs_inner(root.left, sum - root.val)
            dfs_inner(root.right, sum - root.val)
            # 或者在这里写你的逻辑，那就是后序遍历
        def dfs_main(root, sum):
            if not root:
                return
            dfs_inner(root, sum)
            dfs_main(root.left, sum)
            dfs_main(root.right, sum)

        dfs_main(root, sum)
        return self.res