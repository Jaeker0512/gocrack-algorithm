#
# @lc app=leetcode.cn id=61 lang=python3
#
# [61] 旋转链表
#
# https://leetcode-cn.com/problems/rotate-list/description/
#
# algorithms
# Medium (40.63%)
# Likes:    425
# Dislikes: 0
# Total Accepted:    112.9K
# Total Submissions: 277.6K
# Testcase Example:  '[1,2,3,4,5]\n2'
#
# 给定一个链表，旋转链表，将链表每个节点向右移动 k 个位置，其中 k 是非负数。
# 
# 示例 1:
# 
# 输入: 1->2->3->4->5->NULL, k = 2
# 输出: 4->5->1->2->3->NULL
# 解释:
# 向右旋转 1 步: 5->1->2->3->4->NULL
# 向右旋转 2 步: 4->5->1->2->3->NULL
# 
# 
# 示例 2:
# 
# 输入: 0->1->2->NULL, k = 4
# 输出: 2->0->1->NULL
# 解释:
# 向右旋转 1 步: 2->0->1->NULL
# 向右旋转 2 步: 1->2->0->NULL
# 向右旋转 3 步: 0->1->2->NULL
# 向右旋转 4 步: 2->0->1->NULL
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        
        length = 0
        node = head
        while node:
            node = node.next
            length += 1
        if not length:
            return

        if k > length:
            k = k % length
        elif k == length:
            return head

        if not k:
            return head

        k = length - k

        cur = head
        cnt = 1
        mid = None
        dummy = ListNode(-1)
        while cur.next:
            if cnt == k:
                mid = cur
                dummy.next = cur.next
            cur = cur.next
            cnt += 1
        if mid:
            mid.next = None
            cur.next = head
        return dummy.next
        

# @lc code=end

