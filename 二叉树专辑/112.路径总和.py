#
# @lc app=leetcode.cn id=112 lang=python3
#
# [112] 路径总和
#
# https://leetcode-cn.com/problems/path-sum/description/
#
# algorithms
# Easy (51.62%)
# Likes:    495
# Dislikes: 0
# Total Accepted:    165K
# Total Submissions: 319.6K
# Testcase Example:  '[5,4,8,11,null,13,4,7,2,null,null,null,1]\n22'
#
# 给定一个二叉树和一个目标和，判断该树中是否存在根节点到叶子节点的路径，这条路径上所有节点值相加等于目标和。
# 
# 说明: 叶子节点是指没有子节点的节点。
# 
# 示例: 
# 给定如下二叉树，以及目标和 sum = 22，
# 
# ⁠             5
# ⁠            / \
# ⁠           4   8
# ⁠          /   / \
# ⁠         11  13  4
# ⁠        /  \      \
# ⁠       7    2      1
# 
# 
# 返回 true, 因为存在目标和为 22 的根节点到叶子节点的路径 5->4->11->2。
# 
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    ## DFS的解法
    # def hasPathSum(self, root: TreeNode, sum: int) -> bool:
    #     self.validate = False
    #     def dfs(root, sum):
    #         if not root:
    #             return
    #         if not root.left and not root.right:
    #             if sum == root.val:
    #                 self.validate = True
    #         if not self.validate:
    #             dfs(root.left, sum - root.val)
    #             dfs(root.right, sum - root.val)
    #     dfs(root, sum)
    #     return self.validate
    ## BFS的解法
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        self.validate = False
        if not root:
            return self.validate
        q = [(root, 0)]
        while q:
            node, current_sum = q.pop(0)
            current_sum += node.val
            if not node.left and not node.right:
                if current_sum == sum:
                    self.validate = True
                    break
            if node.left:
                q.append((node.left, current_sum))
            if node.right:
                q.append((node.right, current_sum))
        return self.validate

# @lc code=end

