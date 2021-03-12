#
# @lc app=leetcode.cn id=322 lang=python3
#
# [322] 零钱兑换
#
# https://leetcode-cn.com/problems/coin-change/description/
#
# algorithms
# Medium (42.76%)
# Likes:    1112
# Dislikes: 0
# Total Accepted:    191.6K
# Total Submissions: 447.9K
# Testcase Example:  '[1,2,5]\n11'
#
# 给定不同面额的硬币 coins 和一个总金额
# amount。编写一个函数来计算可以凑成总金额所需的最少的硬币个数。如果没有任何一种硬币组合能组成总金额，返回 -1。
# 
# 你可以认为每种硬币的数量是无限的。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：coins = [1, 2, 5], amount = 11
# 输出：3 
# 解释：11 = 5 + 5 + 1
# 
# 示例 2：
# 
# 
# 输入：coins = [2], amount = 3
# 输出：-1
# 
# 示例 3：
# 
# 
# 输入：coins = [1], amount = 0
# 输出：0
# 
# 
# 示例 4：
# 
# 
# 输入：coins = [1], amount = 1
# 输出：1
# 
# 
# 示例 5：
# 
# 
# 输入：coins = [1], amount = 2
# 输出：2
# 
# 
# 
# 
# 提示：
# 
# 
# 1 
# 1 
# 0 
# 
# 
#

# @lc code=start
class Solution:
    ## 递归备忘录解法
    # def coinChange(self, coins: List[int], amount: int) -> int:
    #     memo = dict()
    #     def dp(n):
    #         if n in memo:
    #             return memo[n]
    #         if n == 0:
    #             return 0
    #         if n < 0:
    #             return -1
    #         res = float("INF")
    #         for coin in coins:
    #             sub_problems = dp(n-coin)
    #             if sub_problems == -1:
    #                 continue
    #             res = min(res, 1 + sub_problems)
    #         memo[n] = res if res != float("INF") else -1
    #         return memo[n]
    #     return dp(amount)
    
    ## 迭代动态规划解法0
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount+1 for _ in range(amount+1)]
        dp[0] = 0
        for i in range(len(dp)):
            for coin in coins:
                if i - coin < 0:
                    continue
                dp[i] = min(dp[i], 1+dp[i-coin])
            
        return dp[amount] if dp[amount] != amount+1 else -1
# @lc code=end

