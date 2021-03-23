#
# @lc app=leetcode.cn id=121 lang=python3
#
# [121] 买卖股票的最佳时机
#
# https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock/description/
#
# algorithms
# Easy (56.30%)
# Likes:    1524
# Dislikes: 0
# Total Accepted:    399.6K
# Total Submissions: 708.7K
# Testcase Example:  '[7,1,5,3,6,4]'
#
# 给定一个数组 prices ，它的第 i 个元素 prices[i] 表示一支给定股票第 i 天的价格。
# 
# 你只能选择 某一天 买入这只股票，并选择在 未来的某一个不同的日子 卖出该股票。设计一个算法来计算你所能获取的最大利润。
# 
# 返回你可以从这笔交易中获取的最大利润。如果你不能获取任何利润，返回 0 。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：[7,1,5,3,6,4]
# 输出：5
# 解释：在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
# ⁠    注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格；同时，你不能在买入前卖出股票。
# 
# 
# 示例 2：
# 
# 
# 输入：prices = [7,6,4,3,1]
# 输出：0
# 解释：在这种情况下, 没有交易完成, 所以最大利润为 0。
# 
# 
# 
# 
# 提示：
# 
# 
# 1 
# 0 
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
        # 本地k是固定等于1所以其实可以去掉k这个因素
        n = len(prices)
        # 定义base case
        # dp[0][0] = 0 第0天啥都没开始呢，利润当然是0
        # dp[0][1] = -INF 第0天不可能持有股票，所以利润也用不可能的负无穷表示
        dp_i_0 = 0
        dp_i_1 = float("-INF")
        # 可优化空间
        for i in range(1, n+1):    
            dp_i_0 = max(
                dp_i_0, # rest
                dp_i_1 + prices[i-1] # sell
            ) ## 今天我没有持有股票说明我昨天要么买，要么持有的股票卖掉了
            dp_i_1 = max(
                dp_i_1, # rest
                -prices[i-1] # buy
            ) ## 昨天不持股，今天买入股票（注意：只允许交易一次，因此手上的现金数就是当天的股价的相反数）
            
        return dp_i_0
# @lc code=end

