#
# @lc app=leetcode.cn id=312 lang=python3
#
# [312] 戳气球
#
# https://leetcode-cn.com/problems/burst-balloons/description/
#
# algorithms
# Hard (67.73%)
# Likes:    676
# Dislikes: 0
# Total Accepted:    41.7K
# Total Submissions: 61.5K
# Testcase Example:  '[3,1,5,8]'
#
# 有 n 个气球，编号为0 到 n - 1，每个气球上都标有一个数字，这些数字存在数组 nums 中。
# 
# 现在要求你戳破所有的气球。戳破第 i 个气球，你可以获得 nums[i - 1] * nums[i] * nums[i + 1] 枚硬币。 这里的 i -
# 1 和 i + 1 代表和 i 相邻的两个气球的序号。如果 i - 1或 i + 1 超出了数组的边界，那么就当它是一个数字为 1 的气球。
# 
# 求所能获得硬币的最大数量。
# 
# 
# 示例 1：
# 
# 
# 输入：nums = [3,1,5,8]
# 输出：167
# 解释：
# nums = [3,1,5,8] --> [3,5,8] --> [3,8] --> [8] --> []
# coins =  3*1*5    +   3*5*8   +  1*3*8  + 1*8*1 = 167
# 
# 示例 2：
# 
# 
# 输入：nums = [1,5]
# 输出：10
# 
# 
# 
# 
# 提示：
# 
# 
# n == nums.length
# 1 
# 0 
# 
# 
#

# @lc code=start
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        ## 营造一个开区间的问题
        nums = [1] + nums + [1]
        # 还是要定义dp数组的含义
        # dp[i][j]代表在开区间(i, j)下面把中间的🎈都戳爆所能获得的最大收益
        n = len(nums)
        dp = [[0 for _ in range(n)] for _ in range(n)]
        # 最终要求的就是dp[0][n-1]
        # 由于要求的最终结果在dp表中处于右上角
        # 所以也能确定状态的迭代方向

        for i in range(n-2, -1, -1):
            for j in range(i+1, n):
                for k in range(i+1, j):
                    dp[i][j] = max(dp[i][j], 
                        dp[i][k] + dp[k][j] + nums[i]*nums[j]*nums[k])

        return dp[0][n-1]
# @lc code=end

