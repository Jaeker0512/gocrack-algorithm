#
# @lc app=leetcode.cn id=131 lang=python3
#
# [131] 分割回文串
#
# https://leetcode-cn.com/problems/palindrome-partitioning/description/
#
# algorithms
# Medium (70.39%)
# Likes:    487
# Dislikes: 0
# Total Accepted:    64K
# Total Submissions: 90.9K
# Testcase Example:  '"aab"'
#
# 给定一个字符串 s，将 s 分割成一些子串，使每个子串都是回文串。
# 
# 返回 s 所有可能的分割方案。
# 
# 示例:
# 
# 输入: "aab"
# 输出:
# [
# ⁠ ["aa","b"],
# ⁠ ["a","a","b"]
# ]
# 
#

# @lc code=start
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        track = []

        def is_valid(string):
            left, right = 0, len(string) - 1
            while left < right:
                if string[left] != string[right]:
                    return False
                left += 1
                right -= 1
            return True

        def backtrack(start, s):
            if start >= len(s):
                res.append(track.copy())
            for i in range(start, len(s)):
                cur = s[start:i+1]
                if not is_valid(cur):
                    continue
                track.append(cur)
                backtrack(i+1, s)
                track.pop()

        backtrack(0, s)
        return res
# @lc code=end

