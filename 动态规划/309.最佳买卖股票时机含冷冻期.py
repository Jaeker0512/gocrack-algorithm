#
# @lc app=leetcode.cn id=309 lang=python3
#
# [309] 最佳买卖股票时机含冷冻期
#
# https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/description/
#
# algorithms
# Medium (57.78%)
# Likes:    719
# Dislikes: 0
# Total Accepted:    80K
# Total Submissions: 138.1K
# Testcase Example:  '[1,2,3,0,2]'
#
# 给定一个整数数组，其中第 i 个元素代表了第 i 天的股票价格 。​
# 
# 设计一个算法计算出最大利润。在满足以下约束条件下，你可以尽可能地完成更多的交易（多次买卖一支股票）:
# 
# 
# 你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
# 卖出股票后，你无法在第二天买入股票 (即冷冻期为 1 天)。
# 
# 
# 示例:
# 
# 输入: [1,2,3,0,2]
# 输出: 3 
# 解释: 对应的交易状态为: [买入, 卖出, 冷冻期, 买入, 卖出]
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
        # 这道题含有冷却期1天
        # 所以实际上状态有3个：
        # 0：不持有股票，且不是由于上一天卖出造成的
        # 1：持有股票
        # 2：不持有股票，昨天刚卖出股票，此时不可买卖
        dp_i_0 = 0
        dp_i_2 = 0
        dp_i_1 = float("-INF")
        for i in range(1, n+1):
            tmp = dp_i_0
            dp_i_0 = max(
                dp_i_0, # rest
                dp_i_1 + prices[i-1] # sell
            ) ## 今天我没有持有股票说明我昨天要没买，要么持有的股票卖掉了
            dp_i_1 = max(
                dp_i_1, # rest
                dp_i_2 - prices[i-1] # buy
            ) ## 今天我持有股票说明我昨天要么也持有但是没卖，要么就是新开仓买了股票
            dp_i_2 = tmp
        return dp_i_0
# @lc code=end

