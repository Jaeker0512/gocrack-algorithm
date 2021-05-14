#
# @lc app=leetcode.cn id=148 lang=python3
#
# [148] 排序链表
#
# https://leetcode-cn.com/problems/sort-list/description/
#
# algorithms
# Medium (67.62%)
# Likes:    999
# Dislikes: 0
# Total Accepted:    139.3K
# Total Submissions: 206.2K
# Testcase Example:  '[4,2,1,3]'
#
# 给你链表的头结点 head ，请将其按 升序 排列并返回 排序后的链表 。
# 
# 进阶：
# 
# 
# 你可以在 O(n log n) 时间复杂度和常数级空间复杂度下，对链表进行排序吗？
# 
# 
# 
# 
# 示例 1：
# 
# 
# 输入：head = [4,2,1,3]
# 输出：[1,2,3,4]
# 
# 
# 示例 2：
# 
# 
# 输入：head = [-1,5,3,4,0]
# 输出：[-1,0,3,4,5]
# 
# 
# 示例 3：
# 
# 
# 输入：head = []
# 输出：[]
# 
# 
# 
# 
# 提示：
# 
# 
# 链表中节点的数目在范围 [0, 5 * 10^4] 内
# -10^5 
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
    def sortList(self, head: ListNode) -> ListNode:
        # 先用快排解决一下（会超时）
        def quicksort(head, end):
            if head == end or head.next == end:
                return head
            ## head 即 pivot
            lhead = head
            rtail = head
            cur = head.next

            while cur != end:
                bak_next = cur.next
                if cur.val < head.val:
                    cur.next = lhead
                    lhead = cur
                else:
                    rtail.next = cur
                    rtail = cur
                cur = bak_next

            rtail.next = end
            node = quicksort(lhead, head)
            head.next = quicksort(head.next, end)
            return node
        # return quicksort(head, None)
        # 归并排序（递归版本）
        def merge(node1, node2):
            dummy = cur =  ListNode(-1)
            while node1 and node2:
                if node1.val < node2.val:
                    cur.next = node1
                    node1 = node1.next
                else:
                    cur.next = node2
                    node2 = node2.next
                cur = cur.next
            if node1:
                cur.next = node1
            else:
                cur.next = node2
            return dummy.next
        def mergesort(node):
            if not node or not node.next:
                return node

            ## 利用快慢指针找到cut点
            slow, fast = node, node.next
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            mid = slow.next
            slow.next = None ## cut
            ## 分
            left = mergesort(node)
            right = mergesort(mid)
            ## 合并
            return merge(left, right)
        # return mergesort(head)

        # 归并排序（非递归）
        # head：4->2->1->3
        def mergesort_iteration(head):
            n = 0
            node = head
            while node:
                node = node.next
                n += 1
            res = ListNode(-1)
            res.next = head
            intv = 1 ## 此处的intv为步长
            while intv < n:
                last_tail = res
                cur = res.next

                while cur:
                    ## 记录左半部分起始点
                    left_node = cur
                    i = intv
                    while i and cur:
                        i -= 1
                        cur = cur.next
                    if i:
                        break ## 如果左半部分都不满足的话直接break，再进行下去没有意义且会出错

                    right_node = cur
                    i = intv
                    while i and cur:
                        i -= 1
                        cur = cur.next ## 此时的cur指针已经来到下一对需要合并的链表节点头部了
                    
                    ## 开始合并，这边需要额外的变量c1，c2来帮忙计数
                    c1 = intv   # 左边部分计数肯定等于intv不然直接在上面就break了
                    c2 = intv - i # 右边部分等于它实际有多少个节点

                    while c1 and c2 and left_node and right_node:
                        if left_node.val < right_node.val:
                            small = left_node
                            c1 -= 1
                            left_node = left_node.next
                        else:
                            small = right_node
                            c2 -= 1
                            right_node = right_node.next
                        last_tail.next = small
                        last_tail = last_tail.next
                    if c1 or c2:
                        last_tail.next = left_node if c1 else right_node
                    while c1 > 0 or c2 >0:
                        ## last_tail 贯穿始终
                        last_tail = last_tail.next ## 这边需要把last_tail放到当前这对链表对的尾部
                        c1 -= 1
                        c2 -= 1 
                    last_tail.next = cur ## 别忘记和下一对待合并的链表对进行连接
                intv *= 2
            return res.next

        return mergesort_iteration(head)
                        




 

                

                
# @lc code=end

