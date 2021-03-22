#
# @lc app=leetcode.cn id=198 lang=python3
#
# [198] 打家劫舍
#
# https://leetcode-cn.com/problems/house-robber/description/
#
# algorithms
# Medium (47.89%)
# Likes:    1329
# Dislikes: 0
# Total Accepted:    256.3K
# Total Submissions: 534.1K
# Testcase Example:  '[1,2,3,1]'
#
# 
# 你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。
# 
# 给定一个代表每个房屋存放金额的非负整数数组，计算你 不触动警报装置的情况下 ，一夜之内能够偷窃到的最高金额。
# 
# 
# 
# 示例 1：
# 
# 输入：[1,2,3,1]
# 输出：4
# 解释：偷窃 1 号房屋 (金额 = 1) ，然后偷窃 3 号房屋 (金额 = 3)。
# 偷窃到的最高金额 = 1 + 3 = 4 。
# 
# 示例 2：
# 
# 输入：[2,7,9,3,1]
# 输出：12
# 解释：偷窃 1 号房屋 (金额 = 2), 偷窃 3 号房屋 (金额 = 9)，接着偷窃 5 号房屋 (金额 = 1)。
# 偷窃到的最高金额 = 2 + 9 + 1 = 12 。
# 
# 
# 
# 
# 提示：
# 
# 
# 0 <= nums.length <= 100
# 0 <= nums[i] <= 400
# 
# 
#

# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:  
        n = len(nums)
        ## 先尝试采用递归暴力解决
        # memo = dict()
        # def dp(x, cur_val):
        #     if x in memo:
        #         return memo[x]+cur_val
        #     if x > n-1:
        #         return cur_val
        #     memo[x] = max(dp(x+1, cur_val), 
        #             dp(x+2, cur_val+nums[x]))
        #     return memo[x]
        # return dp(0, 0)

        ## 动态规划尝试，尝试优化空间
        if n == 1:
            return nums[0]
        dp_2 = nums[0]
        dp_1 =  max(nums[0], nums[1])
        for i in range(2, n):
            tmp = max(dp_1, dp_2+nums[i])
            dp_2 = dp_1
            dp_1 = tmp
        return dp_1
# @lc code=end

