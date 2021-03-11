#
# @lc app=leetcode.cn id=58 lang=python3
#
# [58] 最后一个单词的长度
#
# https://leetcode-cn.com/problems/length-of-last-word/description/
#
# algorithms
# Easy (34.25%)
# Likes:    287
# Dislikes: 0
# Total Accepted:    164.2K
# Total Submissions: 479.2K
# Testcase Example:  '"Hello World"'
#
# 给你一个字符串 s，由若干单词组成，单词之间用空格隔开。返回字符串中最后一个单词的长度。如果不存在最后一个单词，请返回 0 。
# 
# 单词 是指仅由字母组成、不包含任何空格字符的最大子字符串。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：s = "Hello World"
# 输出：5
# 
# 
# 示例 2：
# 
# 
# 输入：s = " "
# 输出：0
# 
# 
# 
# 
# 提示：
# 
# 
# 1 
# s 仅有英文字母和空格 ' ' 组成
# 
# 
#

# @lc code=start
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count = 0
        for i in range(len(s)-1, -1, -1):
            if s[i] == ' ':
                if count == 0:
                    continue
                break
            count += 1
        return count


# @lc code=end

