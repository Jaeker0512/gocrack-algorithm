#
# @lc app=leetcode.cn id=86 lang=python3
#
# [86] 分隔链表
#
# https://leetcode-cn.com/problems/partition-list/description/
#
# algorithms
# Medium (62.36%)
# Likes:    362
# Dislikes: 0
# Total Accepted:    88.2K
# Total Submissions: 141.3K
# Testcase Example:  '[1,4,3,2,5,2]\n3'
#
# 给你一个链表的头节点 head 和一个特定值 x ，请你对链表进行分隔，使得所有 小于 x 的节点都出现在 大于或等于 x 的节点之前。
# 
# 你应当 保留 两个分区中每个节点的初始相对位置。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：head = [1,4,3,2,5,2], x = 3
# 输出：[1,2,2,4,3,5]
# 
# 
# 示例 2：
# 
# 
# 输入：head = [2,1], x = 2
# 输出：[1,2]
# 
# 
# 
# 
# 提示：
# 
# 
# 链表中节点的数目在范围 [0, 200] 内
# -100 
# -200 
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
    def partition(self, head: ListNode, x: int) -> ListNode:
        # 输入：head = [1,4,3,2,5,2], x = 3
        # 输出：[1,2,2,4,3,5]
        big = ListNode(-1)
        pre_b = big

        small = ListNode(-2)
        pre_s = small

        cur = head
        while cur:
            if cur.val < x:
                pre_s.next = cur
                pre_s = cur
            else:
                pre_b.next = cur
                pre_b = cur
            cur = cur.next
        pre_b.next = None
        pre_s.next = big.next
        return small.next

# @lc code=end

