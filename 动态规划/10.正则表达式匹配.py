#
# @lc app=leetcode.cn id=10 lang=python3
#
# [10] 正则表达式匹配
#
# https://leetcode-cn.com/problems/regular-expression-matching/description/
#
# algorithms
# Hard (30.95%)
# Likes:    1981
# Dislikes: 0
# Total Accepted:    154.8K
# Total Submissions: 499.3K
# Testcase Example:  '"aa"\n"a"'
#
# 给你一个字符串 s 和一个字符规律 p，请你来实现一个支持 '.' 和 '*' 的正则表达式匹配。
# 
# 
# '.' 匹配任意单个字符
# '*' 匹配零个或多个前面的那一个元素
# 
# 
# 所谓匹配，是要涵盖 整个 字符串 s的，而不是部分字符串。
# 
# 
# 示例 1：
# 
# 
# 输入：s = "aa" p = "a"
# 输出：false
# 解释："a" 无法匹配 "aa" 整个字符串。
# 
# 
# 示例 2:
# 
# 
# 输入：s = "aa" p = "a*"
# 输出：true
# 解释：因为 '*' 代表可以匹配零个或多个前面的那一个元素, 在这里前面的元素就是 'a'。因此，字符串 "aa" 可被视为 'a' 重复了一次。
# 
# 
# 示例 3：
# 
# 
# 输入：s = "ab" p = ".*"
# 输出：true
# 解释：".*" 表示可匹配零个或多个（'*'）任意字符（'.'）。
# 
# 
# 示例 4：
# 
# 
# 输入：s = "aab" p = "c*a*b"
# 输出：true
# 解释：因为 '*' 表示零个或多个，这里 'c' 为 0 个, 'a' 被重复一次。因此可以匹配字符串 "aab"。
# 
# 
# 示例 5：
# 
# 
# 输入：s = "mississippi" p = "mis*is*p*."
# 输出：false
# 
# 
# 
# 提示：
# 
# 
# 0 
# 0 
# s 可能为空，且只包含从 a-z 的小写字母。
# p 可能为空，且只包含从 a-z 的小写字母，以及字符 . 和 *。
# 保证每次出现字符 * 时，前面都匹配到有效的字符
# 
# 
#

# @lc code=start
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # 还是先定义dp数组的含义
        # dp[i][j] 表示 s 的前 i 个是否能被 p 的前 j个匹配
        # dp[i][j]可以由dp[i-1][j-1]转移而来
        # s[i] == p[j] ---> dp[i][j] = dp[i - 1][j - 1]
        # p[i] == . ---> dp[i][j] = dp[i - 1][j - 1]
        # p[i] == * 是难点
        n, m = len(s), len(p)
        dp = [[False for _ in range(m+1)] for _ in range(n+1)]
        dp[0][0] = True
        #当S为空，P不空，要看P是否为 a*b*这种结构
        for j in range(1, m + 1):
            if p[j - 1] == "*":
                dp[0][j] = dp[0][j - 2]

        for i in range(1, n+1):
            for j in range(1, m+1):
                if s[i-1] == p[j-1] or p[j-1] == '.':
                    dp[i][j] = dp[i-1][j-1]
                elif p[j-1] == '*':
                    if p[j-2] == s[i-1] or p[j-2] == '.':
                        dp[i][j] = dp[i - 1][j] or dp[i][j - 2] 
                    else:
                        dp[i][j] = dp[i][j-2] # 此处直接把x*这一段忽略掉了

        return dp[n][m]
# @lc code=end

