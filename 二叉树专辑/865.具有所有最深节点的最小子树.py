#
# @lc app=leetcode.cn id=865 lang=python3
#
# [865] 具有所有最深节点的最小子树
#
# https://leetcode-cn.com/problems/smallest-subtree-with-all-the-deepest-nodes/description/
#
# algorithms
# Medium (61.82%)
# Likes:    107
# Dislikes: 0
# Total Accepted:    5.5K
# Total Submissions: 8.9K
# Testcase Example:  '[3,5,1,6,2,0,8,null,null,7,4]'
#
# 给定一个根为 root 的二叉树，每个节点的深度是 该节点到根的最短距离 。
# 
# 如果一个节点在 整个树 的任意节点之间具有最大的深度，则该节点是 最深的 。
# 
# 一个节点的 子树 是该节点加上它的所有后代的集合。
# 
# 返回能满足 以该节点为根的子树中包含所有最深的节点 这一条件的具有最大深度的节点。
# 
# 
# 
# 注意：本题与力扣 1123
# 重复：https://leetcode-cn.com/problems/lowest-common-ancestor-of-deepest-leaves/
# 
# 
# 
# 示例 1：
# 
# 
# 
# 
# 输入：root = [3,5,1,6,2,0,8,null,null,7,4]
# 输出：[2,7,4]
# 解释：
# 我们返回值为 2 的节点，在图中用黄色标记。
# 在图中用蓝色标记的是树的最深的节点。
# 注意，节点 5、3 和 2 包含树中最深的节点，但节点 2 的子树最小，因此我们返回它。
# 
# 
# 示例 2：
# 
# 
# 输入：root = [1]
# 输出：[1]
# 解释：根节点是树中最深的节点。
# 
# 示例 3：
# 
# 
# 输入：root = [0,1,3,null,2]
# 输出：[2]
# 解释：树中最深的节点为 2 ，有效子树为节点 2、1 和 0 的子树，但节点 2 的子树最小。
# 
# 
# 
# 提示：
# 
# 
# 树中节点的数量介于 1 和 500 之间。
# 0 
# 每个节点的值都是独一无二的。
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
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:

        def dfs(root, depth):
            if not root:
                return depth, root
            l_d, l = dfs(root.left, depth+1)
            r_d, r = dfs(root.right, depth+1)

            if l_d > r_d:
                return l_d, l
            elif l_d < r_d:
                return r_d, r
            else:
                return l_d, root

        return dfs(root, 0)[1]
# @lc code=end

