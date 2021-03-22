#
# @lc app=leetcode.cn id=337 lang=python3
#
# [337] 打家劫舍 III
#
# https://leetcode-cn.com/problems/house-robber-iii/description/
#
# algorithms
# Medium (61.56%)
# Likes:    770
# Dislikes: 0
# Total Accepted:    91.3K
# Total Submissions: 148.2K
# Testcase Example:  '[3,2,3,null,3,null,1]'
#
# 在上次打劫完一条街道之后和一圈房屋后，小偷又发现了一个新的可行窃的地区。这个地区只有一个入口，我们称之为“根”。
# 除了“根”之外，每栋房子有且只有一个“父“房子与之相连。一番侦察之后，聪明的小偷意识到“这个地方的所有房屋的排列类似于一棵二叉树”。
# 如果两个直接相连的房子在同一天晚上被打劫，房屋将自动报警。
# 
# 计算在不触动警报的情况下，小偷一晚能够盗取的最高金额。
# 
# 示例 1:
# 
# 输入: [3,2,3,null,3,null,1]
# 
# ⁠    3
# ⁠   / \
# ⁠  2   3
# ⁠   \   \ 
# ⁠    3   1
# 
# 输出: 7 
# 解释: 小偷一晚能够盗取的最高金额 = 3 + 3 + 1 = 7.
# 
# 示例 2:
# 
# 输入: [3,4,5,1,3,null,1]
# 
# 3
# ⁠   / \
# ⁠  4   5
# ⁠ / \   \ 
# ⁠1   3   1
# 
# 输出: 9
# 解释: 小偷一晚能够盗取的最高金额 = 4 + 5 = 9.
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
    def rob(self, root: TreeNode) -> int:
        ## 因为是二叉树 我们先考虑递归的解法尝试一下
        # memo = dict()
        # def dfs(root):
        #     if root in memo:
        #         return memo[root]
        #     if not root:
        #         return 0
        #     ## 当前节点不抢
        #     res1 = dfs(root.left) + dfs(root.right)
        #     ## 当前节点抢
        #     res2 = root.val
        #     if root.left:
        #         res2 += (dfs(root.left.left) + dfs(root.left.right))
        #     if root.right:
        #         res2 += (dfs(root.right.left) + dfs(root.right.right))
        #     res = max(res1, res2)
        #     memo[root] = res
        #     return res
        # return dfs(root)

        ## 不够快，尝试用树形DP解决，其实就是从数组的遍历转换成
        # 对树的遍历，而树的遍历最常用的就是递归
        # 所以看起来像是动态规划融合了递归一样
        # dfs函数返回的实际上是一个dp table
        # dp[0]代表当前节点不偷的最大收益
        # dp[1]反之        
        def dfs(root):
            if not root:
                return (0, 0)

            left = dfs(root.left)
            right = dfs(root.right)

            # 当前房屋节点偷，那左右节点可不能抢了
            rob_val = root.val + left[0] + right[0]
            # 当前节点不偷，左右节点可偷可不偷，取决于收益
            unrob_val = max(left[0], left[1]) + max(right[0], right[1])

            return (unrob_val, rob_val)
        res = dfs(root)
        return max(res[0], res[1])
    
# @lc code=end

