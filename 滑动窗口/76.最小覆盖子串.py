#
# @lc app=leetcode.cn id=76 lang=python3
#
# [76] 最小覆盖子串
#
# https://leetcode-cn.com/problems/minimum-window-substring/description/
#
# algorithms
# Hard (40.26%)
# Likes:    925
# Dislikes: 0
# Total Accepted:    104.3K
# Total Submissions: 258.3K
# Testcase Example:  '"ADOBECODEBANC"\n"ABC"'
#
# 给你一个字符串 s 、一个字符串 t 。返回 s 中涵盖 t 所有字符的最小子串。如果 s 中不存在涵盖 t 所有字符的子串，则返回空字符串 "" 。
# 
# 注意：如果 s 中存在这样的子串，我们保证它是唯一的答案。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：s = "ADOBECODEBANC", t = "ABC"
# 输出："BANC"
# 
# 
# 示例 2：
# 
# 
# 输入：s = "a", t = "a"
# 输出："a"
# 
# 
# 
# 
# 提示：
# 
# 
# 1 
# s 和 t 由英文字母组成
# 
# 
# 
# 进阶：你能设计一个在 o(n) 时间内解决此问题的算法吗？
#

# @lc code=start
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        from collections import defaultdict
        # 如果不使用defaultdict则需要初始化need字典
        need, window = defaultdict(int), defaultdict(int)
        for c in t:
            need[c] += 1
        # 然后，使用left和right变量初始化窗口的两端，
        # 不要忘了，区间[left, right)是左闭右开的，所以初始情况下窗口没有包含任何元素：
        left, right = 0, 0
        #valid变量表示窗口中满足need条件的字符个数，
        # 如果valid和len(need)的大小相同，则说明窗口已满足条件，已经完全覆盖了串T。
        valid = 0
        s_len = len(s)
        # 1、当移动right扩大窗口，即加入字符时，应该更新哪些数据？
        # 2、什么条件下，窗口应该暂停扩大，开始移动left缩小窗口？
        # 3、当移动left缩小窗口，即移出字符时，应该更新哪些数据？
        # 4、我们要的结果应该在扩大窗口时还是缩小窗口时进行更新？
        # 如果一个字符进入窗口，应该增加window计数器；
        # 如果一个字符将移出窗口的时候，应该减少window计数器；
        # 当valid满足need时应该收缩窗口；应该在收缩窗口的时候更新最终结果。
        start, distance = 0, float("inf")
        while right < s_len:
            # 开始滑动
            # 右移扩大窗口，加入新的字符，更新数据
            char = s[right]
            right += 1
            if char in need:
                window[char] += 1
                if window[char] == need[char]:
                    valid += 1

            while valid == len(need):
                if right - left < distance:
                    start = left
                    distance = right - left
                d_char = s[left]
                left += 1
                if d_char in need:
                    if window[d_char] == need[d_char]:
                        valid -= 1
                    window[d_char] -= 1
        if distance != float("inf"):
            return s[start:start+distance]
        return ""


# @lc code=end

