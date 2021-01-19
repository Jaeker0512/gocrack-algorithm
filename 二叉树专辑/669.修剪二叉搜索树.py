#
# @lc app=leetcode.cn id=669 lang=python3
#
# [669] 修剪二叉搜索树
#
# https://leetcode-cn.com/problems/trim-a-binary-search-tree/description/
#
# algorithms
# Easy (67.10%)
# Likes:    339
# Dislikes: 0
# Total Accepted:    22.5K
# Total Submissions: 33.5K
# Testcase Example:  '[1,0,2]\n1\n2'
#
# 给你二叉搜索树的根节点 root ，同时给定最小边界low 和最大边界 high。通过修剪二叉搜索树，使得所有节点的值在[low,
# high]中。修剪树不应该改变保留在树中的元素的相对结构（即，如果没有被移除，原有的父代子代关系都应当保留）。 可以证明，存在唯一的答案。
# 
# 所以结果应当返回修剪好的二叉搜索树的新的根节点。注意，根节点可能会根据给定的边界发生改变。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：root = [1,0,2], low = 1, high = 2
# 输出：[1,null,2]
# 
# 
# 示例 2：
# 
# 
# 输入：root = [3,0,4,null,2,null,null,1], low = 1, high = 3
# 输出：[3,2,null,1]
# 
# 
# 示例 3：
# 
# 
# 输入：root = [1], low = 1, high = 2
# 输出：[1]
# 
# 
# 示例 4：
# 
# 
# 输入：root = [1,null,2], low = 1, high = 3
# 输出：[1,null,2]
# 
# 
# 示例 5：
# 
# 
# 输入：root = [1,null,2], low = 2, high = 4
# 输出：[2]
# 
# 
# 
# 
# 提示：
# 
# 
# 树中节点数在范围 [1, 10^4] 内
# 0 
# 树中每个节点的值都是唯一的
# 题目数据保证输入是一棵有效的二叉搜索树
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
    def trimBST(self, root: TreeNode, low: int, high: int) -> TreeNode:
        if not root:
            return
        ## 如果当前根节点值小于下限，那包括当前节点以及左边部分字数都需要剪枝去掉，此时只要递归右子树就行了
        if root.val < low:
            root = self.trimBST(root.right, low, high)
        ## 与上面的情况完全相反
        elif root.val > high:
            root = self.trimBST(root.left, low, high)
        ## 当前根节点的值在范围中，那左子树和右子树都需要递归
        else:    
            root.left = self.trimBST(root.left, low, high)
            root.right = self.trimBST(root.right, low, high)
        return root

        
# @lc code=end

