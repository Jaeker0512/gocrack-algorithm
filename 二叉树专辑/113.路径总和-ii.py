#
# @lc app=leetcode.cn id=113 lang=python3
#
# [113] 路径总和 II(剑指 Offer 34. 二叉树中和为某一值的路径)
#
# https://leetcode-cn.com/problems/path-sum-ii/description/
#
# algorithms
# Medium (61.38%)
# Likes:    407
# Dislikes: 0
# Total Accepted:    110.5K
# Total Submissions: 180K
# Testcase Example:  '[5,4,8,11,null,13,4,7,2,null,null,5,1]\n22'
#
# 给定一个二叉树和一个目标和，找到所有从根节点到叶子节点路径总和等于给定目标和的路径。
# 
# 说明: 叶子节点是指没有子节点的节点。
# 
# 示例:
# 给定如下二叉树，以及目标和 sum = 22，
# 
# ⁠             5
# ⁠            / \
# ⁠           4   8
# ⁠          /   / \
# ⁠         11  13  4
# ⁠        /  \    / \
# ⁠       7    2  5   1
# 
# 
# 返回:
# 
# [
# ⁠  [5,4,11,2],
# ⁠  [5,8,4,5]
# ]
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
    ## BFS的解法 队列中的元素除了node以外还需要携带
    # 1、当前的路径（作为结果添加）
    # 2、当前的路径和（用作判断是否满足目标）
    ##
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        res = []
        if not root:
            return res
        queue = [(root, [], 0)]
        while queue:
            root, path, path_sum = queue.pop(0)
            if not root.left and not root.right:
                if path_sum + root.val == sum:
                    res.append((path + [root.val]).copy())
            if root.left:
                queue.append((root.left, path + [root.val], path_sum + root.val))
            if root.right:
                queue.append((root.right, path + [root.val], path_sum + root.val))
        return res
    
    ## DFS的解法 (还可以用回溯法来优化)
    # def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
    #     res = []
    #     def dfs(root, path, sum):
    #         if not root:
    #             return
    #         if not root.left and not root.right: 
    #             if sum == root.val:
    #                 res.append((path + [root.val]).copy())
    #         dfs(root.left, path + [root.val], sum - root.val)
    #         dfs(root.right, path + [root.val], sum - root.val)

    #     dfs(root, [], sum)
    #     return res
    ##
# @lc code=end

