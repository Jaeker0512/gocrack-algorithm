#
# @lc app=leetcode.cn id=583 lang=python3
#
# [583] 两个字符串的删除操作
#
# https://leetcode-cn.com/problems/delete-operation-for-two-strings/description/
#
# algorithms
# Medium (53.27%)
# Likes:    182
# Dislikes: 0
# Total Accepted:    16.1K
# Total Submissions: 30.1K
# Testcase Example:  '"sea"\n"eat"'
#
# 给定两个单词 word1 和 word2，找到使得 word1 和 word2 相同所需的最小步数，每步可以删除任意一个字符串中的一个字符。
# 
# 
# 
# 示例：
# 
# 输入: "sea", "eat"
# 输出: 2
# 解释: 第一步将"sea"变为"ea"，第二步将"eat"变为"ea"
# 
# 
# 
# 
# 提示：
# 
# 
# 给定单词的长度不超过500。
# 给定单词中的字符只含有小写字母。
# 
# 
#

# @lc code=start
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        ## 使用动态规划来做
        # 卧槽，仔细想一想这不就是求最长公共子序列嘛
        # 得到最长公共子序列的长度以后就能得出删除需要的次数了
        n1, n2 = len(word1), len(word2)
        dp = [[0 for _ in range(n2+1)] for _ in range(n1+1)]
        for i in range(1, n1+1):
            for j in range(1, n2+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])

        return n1 + n2 - 2*dp[n1][n2]

# @lc code=end

