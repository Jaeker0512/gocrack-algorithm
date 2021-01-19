#
# @lc app=leetcode.cn id=114 lang=python3
#
# [114] 二叉树展开为链表
#
# https://leetcode-cn.com/problems/flatten-binary-tree-to-linked-list/description/
#
# algorithms
# Medium (71.16%)
# Likes:    631
# Dislikes: 0
# Total Accepted:    93.2K
# Total Submissions: 130.7K
# Testcase Example:  '[1,2,5,3,4,null,6]'
#
# 给定一个二叉树，原地将它展开为一个单链表。
# 
# 
# 
# 例如，给定二叉树
# 
# ⁠   1
# ⁠  / \
# ⁠ 2   5
# ⁠/ \   \
# 3   4   6
# 
# 将其展开为：
# 
# 1
# ⁠\
# ⁠ 2
# ⁠  \
# ⁠   3
# ⁠    \
# ⁠     4
# ⁠      \
# ⁠       5
# ⁠        \
# ⁠         6
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
    def __init__(self):
        self.pre = None
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # def help(root):
        #     if root == None:
        #         return
        #     help(root.right)
        #     help(root.left)

        #     root.right = self.pre
        #     root.left = None
        #     self.pre = root

        # help(root)

        if root == None:
            return
        self.flatten(root.right)
        self.flatten(root.left)

        root.right = self.pre
        root.left = None
        self.pre = root

        
# @lc code=end

