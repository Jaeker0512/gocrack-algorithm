#
# @lc app=leetcode.cn id=387 lang=python3
#
# [387] 字符串中的第一个唯一字符
#
# https://leetcode-cn.com/problems/first-unique-character-in-a-string/description/
#
# algorithms
# Easy (51.46%)
# Likes:    358
# Dislikes: 0
# Total Accepted:    164.1K
# Total Submissions: 318.9K
# Testcase Example:  '"leetcode"'
#
# 给定一个字符串，找到它的第一个不重复的字符，并返回它的索引。如果不存在，则返回 -1。
# 
# 
# 
# 示例：
# 
# s = "leetcode"
# 返回 0
# 
# s = "loveleetcode"
# 返回 2
# 
# 
# 
# 
# 提示：你可以假定该字符串只包含小写字母。
# 
#

# @lc code=start
class Solution:
    def firstUniqChar(self, s: str) -> int:
        valid = [-1 for i in range(26)]

        for i in range(len(s)):
            valid[ord(s[i])-ord('a')] = i
        
        for i in range(len(s)):
            if i == valid[ord(s[i])-ord('a')]:
                return i
            else:
                valid[ord(s[i])-ord('a')] = -1
        return -1
# @lc code=end

