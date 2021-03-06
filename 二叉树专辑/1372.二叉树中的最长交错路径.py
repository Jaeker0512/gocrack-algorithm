#
# @lc app=leetcode.cn id=1372 lang=python3
#
# [1372] 二叉树中的最长交错路径
#
# https://leetcode-cn.com/problems/longest-zigzag-path-in-a-binary-tree/description/
#
# algorithms
# Medium (49.98%)
# Likes:    42
# Dislikes: 0
# Total Accepted:    5.4K
# Total Submissions: 10.8K
# Testcase Example:  '[1,null,1,1,1,null,null,1,1,null,1,null,null,null,1,null,1]'
#
# 给你一棵以 root 为根的二叉树，二叉树中的交错路径定义如下：
# 
# 
# 选择二叉树中 任意 节点和一个方向（左或者右）。
# 如果前进方向为右，那么移动到当前节点的的右子节点，否则移动到它的左子节点。
# 改变前进方向：左变右或者右变左。
# 重复第二步和第三步，直到你在树中无法继续移动。
# 
# 
# 交错路径的长度定义为：访问过的节点数目 - 1（单个节点的路径长度为 0 ）。
# 
# 请你返回给定树中最长 交错路径 的长度。
# 
# 
# 
# 示例 1：
# 
# 
# 
# 输入：root = [1,null,1,1,1,null,null,1,1,null,1,null,null,null,1,null,1]
# 输出：3
# 解释：蓝色节点为树中最长交错路径（右 -> 左 -> 右）。
# 
# 
# 示例 2：
# 
# 
# 
# 输入：root = [1,1,1,null,1,null,null,1,1,null,1]
# 输出：4
# 解释：蓝色节点为树中最长交错路径（左 -> 右 -> 左 -> 右）。
# 
# 
# 示例 3：
# 
# 输入：root = [1]
# 输出：0
# 
# 
# 
# 
# 提示：
# 
# 
# 每棵树最多有 50000 个节点。
# 每个节点的值在 [1, 100] 之间。
# 
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
    def __init__(self):
        self.res = 0

    ## 简单的双递归方法，而且容易超时
    def longestZigZag(self, root: TreeNode) -> int:
        from functools import lru_cache
        @lru_cache(None)
        def dfs_inner(root, dir):
            if not root:
                return 0 
            if dir == -1:
                return  int(root.left != None) + dfs_inner(root.left, dir * -1)
            return int(root.right != None) + dfs_inner(root.right, dir * -1)
            # 或者在这里写你的逻辑，那就是后序遍历
        def dfs_main(root):
            if not root:
                return
            self.res = max(self.res, dfs_inner(root, 1), dfs_inner(root, -1))
            dfs_main(root.left)
            dfs_main(root.right)

        dfs_main(root)
        return self.res
        
# @lc code=end

