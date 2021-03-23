#
# @lc app=leetcode.cn id=714 lang=python3
#
# [714] 买卖股票的最佳时机含手续费
#
# https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/description/
#
# algorithms
# Medium (70.07%)
# Likes:    437
# Dislikes: 0
# Total Accepted:    71K
# Total Submissions: 101.3K
# Testcase Example:  '[1,3,2,8,4,9]\n2'
#
# 给定一个整数数组 prices，其中第 i 个元素代表了第 i 天的股票价格 ；非负整数 fee 代表了交易股票的手续费用。
# 
# 你可以无限次地完成交易，但是你每笔交易都需要付手续费。如果你已经购买了一个股票，在卖出它之前你就不能再继续购买股票了。
# 
# 返回获得利润的最大值。
# 
# 注意：这里的一笔交易指买入持有并卖出股票的整个过程，每笔交易你只需要为支付一次手续费。
# 
# 示例 1:
# 
# 输入: prices = [1, 3, 2, 8, 4, 9], fee = 2
# 输出: 8
# 解释: 能够达到的最大利润:  
# 在此处买入 prices[0] = 1
# 在此处卖出 prices[3] = 8
# 在此处买入 prices[4] = 4
# 在此处卖出 prices[5] = 9
# 总利润: ((8 - 1) - 2) + ((9 - 4) - 2) = 8.
# 
# 注意:
# 
# 
# 0 < prices.length <= 50000.
# 0 < prices[i] < 50000.
# 0 <= fee < 50000.
# 
# 
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        ## 我们需要定义dp table，明确我们的状态和选择
        # dp[i][k][0] 代表现在是第i+1天（i是索引所以+1）
        # 至多完成k次交易，当前状态是不持有股票的情况下的最大收益
        # dp[i][k][1]不是最优的因为持有股票肯定不是最大收益
        # 本道题相当于k是无限大，所以实际上状态转移方程和k也是无关的
        n = len(prices)
        # 最难的是定义base case
        # dp[0][k][0] = 0 第0天啥都没开始呢，利润当然是0
        # dp[0][k][1] = -INF 第0天不可能持有股票，所以利润也用不可能的负无穷表示

        # 记住因为k是无穷大所以k和k-1是一样的
        # 同样也可以进行空间上的优化
        # 唯一不同的是需要把手续费从利润中减去
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
                tmp - prices[i-1] - fee # buy 买卖股票需要的手续费
            ) ## 今天我持有股票说明我昨天要么也持有但是没卖，要么就是新开仓买了股票
        return dp_i_0
# @lc code=end

