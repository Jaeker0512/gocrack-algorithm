#
# @lc app=leetcode.cn id=116 lang=python3
#
# [116] 填充每个节点的下一个右侧节点指针
#
# https://leetcode-cn.com/problems/populating-next-right-pointers-in-each-node/description/
#
# algorithms
# Medium (64.05%)
# Likes:    261
# Dislikes: 0
# Total Accepted:    52.6K
# Total Submissions: 82.1K
# Testcase Example:  '[1,2,3,4,5,6,7]'
#
# 给定一个完美二叉树，其所有叶子节点都在同一层，每个父节点都有两个子节点。二叉树定义如下：
# 
# struct Node {
# ⁠ int val;
# ⁠ Node *left;
# ⁠ Node *right;
# ⁠ Node *next;
# }
# 
# 填充它的每个 next 指针，让这个指针指向其下一个右侧节点。如果找不到下一个右侧节点，则将 next 指针设置为 NULL。
# 
# 初始状态下，所有 next 指针都被设置为 NULL。
# 
# 
# 
# 示例：
# 
# 
# 
# 
# 输入：{"$id":"1","left":{"$id":"2","left":{"$id":"3","left":null,"next":null,"right":null,"val":4},"next":null,"right":{"$id":"4","left":null,"next":null,"right":null,"val":5},"val":2},"next":null,"right":{"$id":"5","left":{"$id":"6","left":null,"next":null,"right":null,"val":6},"next":null,"right":{"$id":"7","left":null,"next":null,"right":null,"val":7},"val":3},"val":1}
# 
# 
# 输出：{"$id":"1","left":{"$id":"2","left":{"$id":"3","left":null,"next":{"$id":"4","left":null,"next":{"$id":"5","left":null,"next":{"$id":"6","left":null,"next":null,"right":null,"val":7},"right":null,"val":6},"right":null,"val":5},"right":null,"val":4},"next":{"$id":"7","left":{"$ref":"5"},"next":null,"right":{"$ref":"6"},"val":3},"right":{"$ref":"4"},"val":2},"next":null,"right":{"$ref":"7"},"val":1}
# 
# 解释：给定二叉树如图 A 所示，你的函数应该填充它的每个 next 指针，以指向其下一个右侧节点，如图 B 所示。
# 
# 
# 
# 
# 提示：
# 
# 
# 你只能使用常量级额外空间。
# 使用递归解题也符合要求，本题中递归程序占用的栈空间不算做额外的空间复杂度。
# 
# 
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    ## DFS的解法
    # def connect(self, root: 'Node') -> 'Node':
    #     if root == None:
    #         return root
    #     if root.left == None:
    #         return root
    

    #     root.left.next = root.right
    #     if root.next:
    #         root.right.next = root.next.left

    #     Solution().connect(root.left)
    #     Solution().connect(root.right)

    #     return root
    ## BFS的解法，是利用了带层的标记模板
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        queue = [root]
        steps = 0
        while queue:
            size = len(queue)
            last_node = None
            for _ in range(size):
                node = queue.pop(0)
                if last_node:
                    last_node.next = node
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                last_node = node
            steps += 1
        return root
# @lc code=end

