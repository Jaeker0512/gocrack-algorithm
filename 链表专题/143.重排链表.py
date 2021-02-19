#
# @lc app=leetcode.cn id=143 lang=python3
#
# [143] 重排链表
#
# https://leetcode-cn.com/problems/reorder-list/description/
#
# algorithms
# Medium (59.50%)
# Likes:    518
# Dislikes: 0
# Total Accepted:    80.1K
# Total Submissions: 134.7K
# Testcase Example:  '[1,2,3,4]'
#
# 给定一个单链表 L：L0→L1→…→Ln-1→Ln ，
# 将其重新排列后变为： L0→Ln→L1→Ln-1→L2→Ln-2→…
# 
# 你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。
# 
# 示例 1:
# 
# 给定链表 1->2->3->4, 重新排列为 1->4->2->3.
# 
# 示例 2:
# 
# 给定链表 1->2->3->4->5, 重新排列为 1->5->2->4->3.
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        help_arr = []
        cur = head
        while cur:
            help_arr.append(cur)
            cur = cur.next

        n = len(help_arr) - 1
        for index, node in enumerate(help_arr):
            if n - index >= index:
                # 保留联系方式
                save = node.next
                node.next = help_arr[n-index]
                help_arr[n- index].next = None
                if n - index > index+1:
                    node.next.next = save
        

        
# @lc code=end

