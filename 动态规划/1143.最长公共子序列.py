#
# @lc app=leetcode.cn id=1143 lang=python3
#
# [1143] 最长公共子序列
#
# https://leetcode-cn.com/problems/longest-common-subsequence/description/
#
# algorithms
# Medium (61.25%)
# Likes:    404
# Dislikes: 0
# Total Accepted:    79.3K
# Total Submissions: 129.3K
# Testcase Example:  '"abcde"\n"ace"'
#
# 给定两个字符串 text1 和 text2，返回这两个字符串的最长公共子序列的长度。
# 
# 一个字符串的 子序列 是指这样一个新的字符串：它是由原字符串在不改变字符的相对顺序的情况下删除某些字符（也可以不删除任何字符）后组成的新字符串。
# 例如，"ace" 是 "abcde" 的子序列，但 "aec" 不是 "abcde"
# 的子序列。两个字符串的「公共子序列」是这两个字符串所共同拥有的子序列。
# 
# 若这两个字符串没有公共子序列，则返回 0。
# 
# 
# 
# 示例 1:
# 
# 输入：text1 = "abcde", text2 = "ace" 
# 输出：3  
# 解释：最长公共子序列是 "ace"，它的长度为 3。
# 
# 
# 示例 2:
# 
# 输入：text1 = "abc", text2 = "abc"
# 输出：3
# 解释：最长公共子序列是 "abc"，它的长度为 3。
# 
# 
# 示例 3:
# 
# 输入：text1 = "abc", text2 = "def"
# 输出：0
# 解释：两个字符串没有公共子序列，返回 0。
# 
# 
# 
# 
# 提示:
# 
# 
# 1 <= text1.length <= 1000
# 1 <= text2.length <= 1000
# 输入的字符串只含有小写英文字符。
# 
# 
#

# @lc code=start
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # 直接用动态规划来干就得了
        # 还是先定义dp数组的含义
        # dp[i][j]代表的是以A[i]和B[i]为末尾项的最长公共子序列长度
        # 如果它们俩一样，以它们俩为末尾项的公共子序列，长度保底为1——dp[i][j]至少为 1，
        # 要考虑它们俩的前缀数组——dp[i-1][j-1]能为它们俩提供多大的公共长度
        a, b = len(text1), len(text2)
        dp = [[0 for _ in range(b+1)] for _ in range(a+1)]
        for i in range(1, a+1):
            for j in range(1, b+1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    # 如果不相等证明text1[i-1]和text[j-1]至少有一个
                    # 不在最长公共子序列当中，记住这一点！！！
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[a][b]
        ## 可优化空间的
# @lc code=end

