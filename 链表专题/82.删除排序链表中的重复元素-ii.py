#
# @lc app=leetcode.cn id=82 lang=python3
#
# [82] 删除排序链表中的重复元素 II
#
# https://leetcode-cn.com/problems/remove-duplicates-from-sorted-list-ii/description/
#
# algorithms
# Medium (50.15%)
# Likes:    454
# Dislikes: 0
# Total Accepted:    85.4K
# Total Submissions: 169.9K
# Testcase Example:  '[1,2,3,3,4,4,5]'
#
# 给定一个排序链表，删除所有含有重复数字的节点，只保留原始链表中 没有重复出现 的数字。
# 
# 示例 1:
# 
# 输入: 1->2->3->3->4->4->5
# 输出: 1->2->5
# 
# 
# 示例 2:
# 
# 输入: 1->1->1->2->3
# 输出: 2->3
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        dummy = ListNode(-1)
        dummy.next = head

        l = dummy
        r = head

        while r and r.next:
            if l.next.val != r.next.val:
                l = l.next
            else:
                while r and r.next and l.next.val == r.next.val:
                    r = r.next
                l.next = r.next
            r = r.next

        return dummy.next
# @lc code=end

