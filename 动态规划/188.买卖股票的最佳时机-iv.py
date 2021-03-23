#
# @lc app=leetcode.cn id=188 lang=python3
#
# [188] 买卖股票的最佳时机 IV
#
# https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-iv/description/
#
# algorithms
# Hard (36.68%)
# Likes:    472
# Dislikes: 0
# Total Accepted:    64.2K
# Total Submissions: 174.7K
# Testcase Example:  '2\n[2,4,1]'
#
# 给定一个整数数组 prices ，它的第 i 个元素 prices[i] 是一支给定的股票在第 i 天的价格。
# 
# 设计一个算法来计算你所能获取的最大利润。你最多可以完成 k 笔交易。
# 
# 注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：k = 2, prices = [2,4,1]
# 输出：2
# 解释：在第 1 天 (股票价格 = 2) 的时候买入，在第 2 天 (股票价格 = 4) 的时候卖出，这笔交易所能获得利润 = 4-2 = 2 。
# 
# 示例 2：
# 
# 
# 输入：k = 2, prices = [3,2,6,5,0,3]
# 输出：7
# 解释：在第 2 天 (股票价格 = 2) 的时候买入，在第 3 天 (股票价格 = 6) 的时候卖出, 这笔交易所能获得利润 = 6-2 = 4 。
# ⁠    随后，在第 5 天 (股票价格 = 0) 的时候买入，在第 6 天 (股票价格 = 3) 的时候卖出, 这笔交易所能获得利润 = 3-0 = 3
# 。
# 
# 
# 
# 提示：
# 
# 
# 0 
# 0 
# 0 
# 
# 
#

# @lc code=start
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        ## 我们需要定义dp table，明确我们的状态和选择
        # dp[i][k][0] 代表现在是第i+1天（i是索引所以+1）
        # 至多完成k次交易，当前状态是不持有股票的情况下的最大收益
        # dp[i][k][1]不是最优的因为持有股票肯定不是最大收益
        n = len(prices)
        max_k = k
        dp = [[0, float("-INF")] for _ in range(max_k+1)]

        # 最难的是定义base case
        # dp[0][k][0] = 0 第0天啥都没开始呢，利润当然是0
        # dp[0][k][1] = -INF 第0天不可能持有股票，所以利润也用不可能的负无穷表示
        # dp[i][0][0] = 0 k是至今最大允许交易次数，如果是0的话意味着不允许交易何来利润
        # dp[i][0][1] = -INF 都不允许交易了，哪里的持有股票，用不可能的负无穷来表示

        # 最典型的模板
        # for i in range(1, n+1):
        #     for k in range(1, max_k+1):
        #         dp[i][k][0] = max(
        #             dp[i-1][k][0], # rest
        #             dp[i-1][k][1] + prices[i-1] # sell
        #         ) ## 今天我没有持有股票说明我昨天要么买，要么持有的股票卖掉了
        #         dp[i][k][1] = max(
        #             dp[i-1][k][1], # rest
        #             dp[i-1][k-1][0] - prices[i-1] # buy
        #         ) ## 今天我持有股票说明我昨天要么也持有但是没卖，要么就是新开仓买了股票
        # return dp[n][k][0]
        # 优化空间版本
        # 同时还应该考虑dp数组的空间问题，如果k过大，就等同于k是无限大
        def help(prices):
            n = len(prices)
            dp_i_0 = 0
            dp_i_1 = float("-INF")
            for i in range(1, n+1):
                tmp = dp_i_0
                dp_i_0 = max(
                    dp_i_0, # rest
                    dp_i_1 + prices[i-1] # sell
                ) ## 今天我没有持有股票说明我昨天要么买，要么持有的股票卖掉了
                dp_i_1 = max(
                    dp_i_1, # rest
                    tmp - prices[i-1] # buy
                ) ## 今天我持有股票说明我昨天要么也持有但是没卖，要么就是新开仓买了股票
            return dp_i_0
        if k > n//2:
            return help(prices)

        for i in range(1, n+1):
            for k in range(max_k, 0, -1):
                dp[k][0] = max(
                    dp[k][0], # rest
                    dp[k][1] + prices[i-1] # sell
                ) ## 今天我没有持有股票说明我昨天要么买，要么持有的股票卖掉了
                dp[k][1] = max(
                    dp[k][1], # rest
                    dp[k-1][0] - prices[i-1] # buy
                ) ## 今天我持有股票说明我昨天要么也持有但是没卖，要么就是新开仓买了股票
        return dp[max_k][0]
# @lc code=end

