#
# @lc app=leetcode.cn id=92 lang=python3
#
# [92] 反转链表 II
#
# https://leetcode-cn.com/problems/reverse-linked-list-ii/description/
#
# algorithms
# Medium (52.15%)
# Likes:    674
# Dislikes: 0
# Total Accepted:    102.5K
# Total Submissions: 195.9K
# Testcase Example:  '[1,2,3,4,5]\n2\n4'
#
# 反转从位置 m 到 n 的链表。请使用一趟扫描完成反转。
# 
# 说明:
# 1 ≤ m ≤ n ≤ 链表长度。
# 
# 示例:
# 
# 输入: 1->2->3->4->5->NULL, m = 2, n = 4
# 输出: 1->4->3->2->5->NULL
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        count = 1
        def help(head):
            pre = None
            cur = head
            while cur:
                # 留下联系方式
                next = cur.next
                # 修改指针
                cur.next = pre
                # 继续往下走
                pre = cur
                cur = next
            return head, pre
        
        pre = None
        cur = head
        while cur:
            if count == m:
                a = pre
                pre_head = cur
            if count == n:
                d = cur.next
                cur.next = None
                break
            pre = cur
            cur = cur.next
            count += 1
        b, c = help(pre_head)

        if a:
            a.next = c
        if b:
            b.next = d
        if a:
            return head
        else:
            return c
        
# @lc code=end

