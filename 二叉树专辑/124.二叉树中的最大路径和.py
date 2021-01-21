#
# @lc app=leetcode.cn id=124 lang=python3
#
# [124] 二叉树中的最大路径和
#
# https://leetcode-cn.com/problems/binary-tree-maximum-path-sum/description/
#
# algorithms
# Hard (43.25%)
# Likes:    853
# Dislikes: 0
# Total Accepted:    93K
# Total Submissions: 215K
# Testcase Example:  '[1,2,3]'
#
# 路径 被定义为一条从树中任意节点出发，沿父节点-子节点连接，达到任意节点的序列。该路径 至少包含一个 节点，且不一定经过根节点。
# 
# 路径和 是路径中各节点值的总和。
# 
# 给你一个二叉树的根节点 root ，返回其 最大路径和 。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：root = [1,2,3]
# 输出：6
# 解释：最优路径是 2 -> 1 -> 3 ，路径和为 2 + 1 + 3 = 6
# 
# 示例 2：
# 
# 
# 输入：root = [-10,9,20,null,null,15,7]
# 输出：42
# 解释：最优路径是 15 -> 20 -> 7 ，路径和为 15 + 20 + 7 = 42
# 
# 
# 
# 
# 提示：
# 
# 
# 树中节点数目范围是 [1, 3 * 10^4]
# -1000 
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
    def maxPathSum(self, root: TreeNode) -> int:
        self.max_sum = float('-inf')
    # 路径停在当前子树的根节点，收益：root.val
    # 走入左子树，最大收益：root.val + dfs(root.left)
    # 走入右子树，最大收益：root.val + dfs(root.right)
    # 再次提醒: 一条从父节点延伸下来的路径，不能走入左子树又掉头走右子树，不能两头收益。
    # 当遍历到null节点时，返回 0，收益为 0。
    # 如果子树 dfs 返回负值，走入它，收益反减，该子树应被忽略，让它返回 0，如同砍掉
        def dfs(root):
            if not root:
                return 0
            # 注意！！！一个子树内部的路径，要包含当前子树的根节点（只是不必一定要从根节点出发的子树）
            # 如果不包含，那还算什么属于当前子树的路径，而是当前子树的子树的内部路径。
            # 所以，一个子树内部的最大路径和 = 左子树提供的最大路径和 + 根节点值 + 右子树提供的最大路径和。
            # 即 dfs(root.left) + root.val + dfs(root.right);
            l = dfs(root.left)
            r = dfs(root.right)
            current_max = l + r + root.val
            self.max_sum = max(self.max_sum, current_max)
            out_max = root.val + max(l , r)
            if out_max < 0:
                return 0
            else:
                return out_max
        dfs(root)
        return self.max_sum

# @lc code=end

