#
# @lc app=leetcode.cn id=173 lang=python3
#
# [173] 二叉搜索树迭代器
#
# https://leetcode-cn.com/problems/binary-search-tree-iterator/description/
#
# algorithms
# Medium (80.14%)
# Likes:    453
# Dislikes: 0
# Total Accepted:    67K
# Total Submissions: 83.6K
# Testcase Example:  '["BSTIterator","next","next","hasNext","next","hasNext","next","hasNext","next","hasNext"]\n' +
  # [[[7,3,15,null,null,9,20]],[],[],[],[],[],[],[],[],[]]
#
# 实现一个二叉搜索树迭代器类BSTIterator ，表示一个按中序遍历二叉搜索树（BST）的迭代器：
# 
# 
# 
# BSTIterator(TreeNode root) 初始化 BSTIterator 类的一个对象。BST 的根节点 root
# 会作为构造函数的一部分给出。指针应初始化为一个不存在于 BST 中的数字，且该数字小于 BST 中的任何元素。
# boolean hasNext() 如果向指针右侧遍历存在数字，则返回 true ；否则返回 false 。
# int next()将指针向右移动，然后返回指针处的数字。
# 
# 
# 注意，指针初始化为一个不存在于 BST 中的数字，所以对 next() 的首次调用将返回 BST 中的最小元素。
# 
# 
# 
# 你可以假设 next() 调用总是有效的，也就是说，当调用 next() 时，BST 的中序遍历中至少存在一个下一个数字。
# 
# 
# 
# 示例：
# 
# 
# 输入
# ["BSTIterator", "next", "next", "hasNext", "next", "hasNext", "next",
# "hasNext", "next", "hasNext"]
# [[[7, 3, 15, null, null, 9, 20]], [], [], [], [], [], [], [], [], []]
# 输出
# [null, 3, 7, true, 9, true, 15, true, 20, false]
# 
# 解释
# BSTIterator bSTIterator = new BSTIterator([7, 3, 15, null, null, 9, 20]);
# bSTIterator.next();    // 返回 3
# bSTIterator.next();    // 返回 7
# bSTIterator.hasNext(); // 返回 True
# bSTIterator.next();    // 返回 9
# bSTIterator.hasNext(); // 返回 True
# bSTIterator.next();    // 返回 15
# bSTIterator.hasNext(); // 返回 True
# bSTIterator.next();    // 返回 20
# bSTIterator.hasNext(); // 返回 False
# 
# 
# 
# 
# 提示：
# 
# 
# 树中节点的数目在范围 [1, 10^5] 内
# 0 
# 最多调用 10^5 次 hasNext 和 next 操作
# 
# 
# 
# 
# 进阶：
# 
# 
# 你可以设计一个满足下述条件的解决方案吗？next() 和 hasNext() 操作均摊时间复杂度为 O(1) ，并使用 O(h) 内存。其中 h
# 是树的高度。
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
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class BSTIterator:

    def __init__(self, root: TreeNode):
        def get_min(root):
            if not root.left:
                first = TreeNode(root.val-1)
                first.right = root
                return first
            left = get_min(root.left)
            return left
        
        first_node = get_min(root)
        dummy = ListNode(first_node.val-1)
        self.pre = dummy
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            cur = ListNode(node.val)
            self.pre.next = cur
            self.pre = cur
            dfs(node.right)

        dfs(root)
        self.cur = dummy

    def next(self) -> int:
        self.cur = self.cur.next
        res = self.cur.val
        return res


    def hasNext(self) -> bool:
        if self.cur.next:
            return True
        return False



# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
# @lc code=end

