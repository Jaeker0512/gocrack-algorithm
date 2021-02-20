#
# @lc app=leetcode.cn id=25 lang=python3
#
# [25] K 个一组翻转链表
#
# https://leetcode-cn.com/problems/reverse-nodes-in-k-group/description/
#
# algorithms
# Hard (64.01%)
# Likes:    909
# Dislikes: 0
# Total Accepted:    134.6K
# Total Submissions: 210K
# Testcase Example:  '[1,2,3,4,5]\n2'
#
# 给你一个链表，每 k 个节点一组进行翻转，请你返回翻转后的链表。
# 
# k 是一个正整数，它的值小于或等于链表的长度。
# 
# 如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。
# 
# 
# 
# 示例：
# 
# 给你这个链表：1->2->3->4->5
# 
# 当 k = 2 时，应当返回: 2->1->4->3->5
# 
# 当 k = 3 时，应当返回: 3->2->1->4->5
# 
# 
# 
# 说明：
# 
# 
# 你的算法只能使用常数的额外空间。
# 你不能只是单纯的改变节点内部的值，而是需要实际进行节点交换。
# 
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # 记得画图，采用4点法
    # 当触发条件时dummy为p1，cur其实是p3
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        def reverse(p1, p4):
            pre = p1
            p2 = cur = p1.next
            while cur != p4:
                next = cur.next
                cur.next = pre
                pre = cur
                cur = next
            p1.next = pre
            p2.next = p4
            return p2
        
        if not head:
            return

        dummy = ListNode(-1)
        dummy.next = head
        count = 0
        cur = head
        pre = dummy
        while cur:
            count += 1
            if count % k == 0:
                pre = reverse(pre, cur.next)
                cur = pre.next
            else:
                cur = cur.next
        return dummy.next
# @lc code=end

