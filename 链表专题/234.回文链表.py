#
# @lc app=leetcode.cn id=234 lang=python3
#
# [234] 回文链表
#
# https://leetcode-cn.com/problems/palindrome-linked-list/description/
#
# algorithms
# Easy (45.40%)
# Likes:    862
# Dislikes: 0
# Total Accepted:    196.7K
# Total Submissions: 432.5K
# Testcase Example:  '[1,2]'
#
# 请判断一个链表是否为回文链表。
# 
# 示例 1:
# 
# 输入: 1->2
# 输出: false
# 
# 示例 2:
# 
# 输入: 1->2->2->1
# 输出: true
# 
# 
# 进阶：
# 你能否用 O(n) 时间复杂度和 O(1) 空间复杂度解决此题？
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        def reverse(head):
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
            return pre
        
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        if fast:
            slow = slow.next
        left = head
        right = reverse(slow)

        while left and right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        return True

# @lc code=end

