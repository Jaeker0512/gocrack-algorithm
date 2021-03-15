#
# @lc app=leetcode.cn id=343 lang=python3
#
# [343] 整数拆分
#
# https://leetcode-cn.com/problems/integer-break/description/
#
# algorithms
# Medium (59.39%)
# Likes:    459
# Dislikes: 0
# Total Accepted:    77.4K
# Total Submissions: 130.4K
# Testcase Example:  '2'
#
# 给定一个正整数 n，将其拆分为至少两个正整数的和，并使这些整数的乘积最大化。 返回你可以获得的最大乘积。
# 
# 示例 1:
# 
# 输入: 2
# 输出: 1
# 解释: 2 = 1 + 1, 1 × 1 = 1。
# 
# 示例 2:
# 
# 输入: 10
# 输出: 36
# 解释: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36。
# 
# 说明: 你可以假设 n 不小于 2 且不大于 58。
# 
#

# @lc code=start
class Solution:
    def integerBreak(self, n: int) -> int:
        ## 递归备忘录 解法
        # memo = dict()
        # def dp(n):
        #     if n in memo:
        #         return memo[n]
        #     max_value = 1
        #     for i in range(1, n):
        #         max_value = max(max_value, (n-i)*i, dp(n-i)*i)
        #     memo[n] = max_value
        #     return memo[n]
        # return dp(n)
        ## dp table 解法
        # dp = [1 for _ in range(n+1)]
        # dp[2] = 1
        # for i in range(3, n+1):
        #     for j in range(1, i):
        #         dp[i] = max((i - j)*j, dp[i - j]*j, dp[i])
        # return dp[n]
        ## 数学法 均值不等式
        import math
        if n <= 3:
            return n - 1
        a = int(n/3)
        b = n % 3
        if b == 0:
            return int(math.pow(3, a))
        elif b == 1:
            return int(math.pow(3, a-1)*4)
        else:
            return int(math.pow(3, a)*2)
        
# @lc code=end

