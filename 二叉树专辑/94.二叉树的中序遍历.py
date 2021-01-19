#
# @lc app=leetcode.cn id=94 lang=python3
#
# [94] 二叉树的中序遍历
#
# https://leetcode-cn.com/problems/binary-tree-inorder-traversal/description/
#
# algorithms
# Medium (73.77%)
# Likes:    740
# Dislikes: 0
# Total Accepted:    279.3K
# Total Submissions: 378.6K
# Testcase Example:  '[1,null,2,3]'
#
# 给定一个二叉树，返回它的中序 遍历。
# 
# 示例:
# 
# 输入: [1,null,2,3]
# ⁠  1
# ⁠   \
# ⁠    2
# ⁠   /
# ⁠  3
# 
# 输出: [1,3,2]
# 
# 进阶: 递归算法很简单，你可以通过迭代算法完成吗？
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
        self.out = []
    ## 递归方法
    # def inorderTraversal(self, root: TreeNode) -> List[int]:
    #     if not root:
    #         return
        
    #     self.inorderTraversal(root.left)
    #     self.out.append(root.val)
    #     self.inorderTraversal(root.right)

    #     return self.out

    ## 迭代方法
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        WHITE, GRAY = 0, 1
        stack = [(WHITE, root)]

        while stack:
            color, node = stack.pop()
            if not node:
                continue
            if color == WHITE:
                stack.append((WHITE, node.right))
                stack.append((GRAY, node))
                stack.append((WHITE, node.left))
            else:
                res.append(node.val)
        return res
# @lc code=end

