#
# @lc app=leetcode.cn id=1026 lang=python3
#
# [1026] 节点与其祖先之间的最大差值
#
# https://leetcode-cn.com/problems/maximum-difference-between-node-and-ancestor/description/
#
# algorithms
# Medium (64.82%)
# Likes:    73
# Dislikes: 0
# Total Accepted:    7.6K
# Total Submissions: 11.7K
# Testcase Example:  '[8,3,10,1,6,null,14,null,null,4,7,13]'
#
# 给定二叉树的根节点 root，找出存在于 不同 节点 A 和 B 之间的最大值 V，其中 V = |A.val - B.val|，且 A 是 B
# 的祖先。
# 
# （如果 A 的任何子节点之一为 B，或者 A 的任何子节点是 B 的祖先，那么我们认为 A 是 B 的祖先）
# 
# 
# 
# 示例 1：
# 
# 
# 
# 
# 输入：root = [8,3,10,1,6,null,14,null,null,4,7,13]
# 输出：7
# 解释： 
# 我们有大量的节点与其祖先的差值，其中一些如下：
# |8 - 3| = 5
# |3 - 7| = 4
# |8 - 1| = 7
# |10 - 13| = 3
# 在所有可能的差值中，最大值 7 由 |8 - 1| = 7 得出。
# 
# 
# 示例 2：
# 
# 
# 输入：root = [1,null,2,null,0,3]
# 输出：3
# 
# 
# 
# 
# 提示：
# 
# 
# 树中的节点数在 2 到 5000 之间。
# 0 
# 
# 
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        self.max_value = float("-inf")
        def dfs(root, min_value , max_value):
            if not root:
                return
            self.max_value = max(abs(root.val - min_value), abs(root.val - max_value), self.max_value)
            if root.val < min_value:
                min_value = root.val
            elif root.val > max_value:
                max_value = root.val
            dfs(root.left, min_value, max_value)
            dfs(root.right, min_value, max_value)

        dfs(root, root.val, root.val)
        return self.max_value
# @lc code=end

