#
# @lc app=leetcode.cn id=122 lang=python3
#
# [122] 买卖股票的最佳时机 II
#
# https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-ii/description/
#
# algorithms
# Easy (66.94%)
# Likes:    1153
# Dislikes: 0
# Total Accepted:    326.1K
# Total Submissions: 486.5K
# Testcase Example:  '[7,1,5,3,6,4]'
#
# 给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。
# 
# 设计一个算法来计算你所能获取的最大利润。你可以尽可能地完成更多的交易（多次买卖一支股票）。
# 
# 注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
# 
# 
# 
# 示例 1:
# 
# 输入: [7,1,5,3,6,4]
# 输出: 7
# 解释: 在第 2 天（股票价格 = 1）的时候买入，在第 3 天（股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。
# 随后，在第 4 天（股票价格 = 3）的时候买入，在第 5 天（股票价格 = 6）的时候卖出, 这笔交易所能获得利润 = 6-3 = 3 。
# 
# 
# 示例 2:
# 
# 输入: [1,2,3,4,5]
# 输出: 4
# 解释: 在第 1 天（股票价格 = 1）的时候买入，在第 5 天 （股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。
# 注意你不能在第 1 天和第 2 天接连购买股票，之后再将它们卖出。
# 因为这样属于同时参与了多笔交易，你必须在再次购买前出售掉之前的股票。
# 
# 
# 示例 3:
# 
# 输入: [7,6,4,3,1]
# 输出: 0
# 解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。
# 
# 
# 
# 提示：
# 
# 
# 1 <= prices.length <= 3 * 10 ^ 4
# 0 <= prices[i] <= 10 ^ 4
# 
# 
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
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
# @lc code=end

