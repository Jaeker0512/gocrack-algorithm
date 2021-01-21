#
# @lc app=leetcode.cn id=894 lang=python3
#
# [894] 所有可能的满二叉树
#
# https://leetcode-cn.com/problems/all-possible-full-binary-trees/description/
#
# algorithms
# Medium (76.90%)
# Likes:    176
# Dislikes: 0
# Total Accepted:    10K
# Total Submissions: 13K
# Testcase Example:  '7'
#
# 满二叉树是一类二叉树，其中每个结点恰好有 0 或 2 个子结点。
# 
# 返回包含 N 个结点的所有可能满二叉树的列表。 答案的每个元素都是一个可能树的根结点。
# 
# 答案中每个树的每个结点都必须有 node.val=0。
# 
# 你可以按任何顺序返回树的最终列表。
# 
# 
# 
# 示例：
# 
# 输入：7
# 
# 输出：[[0,0,0,null,null,0,0,null,null,0,0],[0,0,0,null,null,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,null,null,null,null,0,0],[0,0,0,0,0,null,null,0,0]]
# 解释：
# 
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= N <= 20
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
    # 对于这个问题来说，结束条件为：
    # 当 N 为偶数时：无法构造满二叉树，返回空数组
    # 当 N == 1 时：树只有一个节点，直接返回包含这个节点的数组
    # 当完成 N 个节点满二叉树构造时：返回结果数组
    # 当需要构造左右子树时，就进行自身调用。
    # 核心观念，递归！！！，左子树构建也是满二叉树，左子树的左右子树也是满二叉树
    # 右子树构建也是满二叉树，右子树的左右子树也是满二叉树
    def allPossibleFBT(self, N: int) -> List[TreeNode]:
        res = []
        if N % 2 == 0:
            return []
        if N == 1:
            return [TreeNode(0)]

        # 左子树分配一个节点
        left_num = 1
        # 右子树可以分配到 N - 1 - 1 = N - 2 个节点
        right_num = N - 2
        while right_num > 0:
            left_tree = self.allPossibleFBT(left_num)
            right_tree = self.allPossibleFBT(right_num)
            for i in range(len(left_tree)):
                for j in range(len(right_tree)):
                    root = TreeNode(0)
                    root.left = left_tree[i]
                    root.right = right_tree[j]
                    res.append(root)
            left_num += 2
            right_num -= 2

        return res


        
# @lc code=end

