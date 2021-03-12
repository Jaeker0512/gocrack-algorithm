#
# @lc app=leetcode.cn id=72 lang=python3
#
# [72] 编辑距离
#
# https://leetcode-cn.com/problems/edit-distance/description/
#
# algorithms
# Hard (60.57%)
# Likes:    1453
# Dislikes: 0
# Total Accepted:    113.8K
# Total Submissions: 187.8K
# Testcase Example:  '"horse"\n"ros"'
#
# 给你两个单词 word1 和 word2，请你计算出将 word1 转换成 word2 所使用的最少操作数 。
# 
# 你可以对一个单词进行如下三种操作：
# 
# 
# 插入一个字符
# 删除一个字符
# 替换一个字符
# 
# 
# 
# 
# 示例 1：
# 
# 
# 输入：word1 = "horse", word2 = "ros"
# 输出：3
# 解释：
# horse -> rorse (将 'h' 替换为 'r')
# rorse -> rose (删除 'r')
# rose -> ros (删除 'e')
# 
# 
# 示例 2：
# 
# 
# 输入：word1 = "intention", word2 = "execution"
# 输出：5
# 解释：
# intention -> inention (删除 't')
# inention -> enention (将 'i' 替换为 'e')
# enention -> exention (将 'n' 替换为 'x')
# exention -> exection (将 'n' 替换为 'c')
# exection -> execution (插入 'u')
# 
# 
# 
# 
# 提示：
# 
# 
# 0 
# word1 和 word2 由小写英文字母组成
# 
# 
#

# @lc code=start
class Solution:
    ## 递归备忘录 解法
    # def minDistance(self, word1: str, word2: str) -> int:
    #     memo = dict()
    #     def dp(i, j):
    #         if (i, j) in memo:
    #             return memo[(i, j)]
    #         # base case
    #         if i == -1:
    #             return j + 1 # 如果s1串已经走完，剩余的只能全部插入了，操作数就是j+1
    #         if j == -1:
    #             return i + 1 # 如果s2串已经走完，剩余的只能全部删除看，操作数就是i+1
    #         if word1[i] == word2[j]:
    #             memo[(i, j)] = dp(i - 1, j - 1)
    #         else:
    #             memo[(i, j)] =  min(
    #                         dp(i, j - 1) + 1,    # 插入操作 
    #                         dp(i - 1, j) + 1,    # 删除操作
    #                         dp(i - 1, j - 1) + 1 # 替换操作
    #                         )
    #         return memo[(i, j)]
    #     return dp(len(word1) - 1, len(word2) - 1)
    
    ## dp table 解法
    def minDistance(self, word1: str, word2: str) -> int:
        n1, n2 = len(word1), len(word2)
        dp = [[0 for _ in range(n2+1)] for _ in range(n1+1)]

        for j in range(1, n2 + 1):
            dp[0][j] = j # 如果s1串已经走完，剩余的只能全部插入了，操作数就是j
        for i in range(1, n1 + 1):
            dp[i][0] = i # 如果s2串已经走完，剩余的只能全部删除看，操作数就是i

        for i in range(1, n1+1):
            for j in range(1, n2+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(
                            dp[i][j - 1],    # 插入操作 
                            dp[i - 1][j],    # 删除操作
                            dp[i - 1][j - 1] # 替换操作
                            ) + 1
        return dp[n1][n2]
# @lc code=end

