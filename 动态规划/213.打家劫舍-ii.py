#
# @lc app=leetcode.cn id=213 lang=python3
#
# [213] 打家劫舍 II
#
# https://leetcode-cn.com/problems/house-robber-ii/description/
#
# algorithms
# Medium (41.04%)
# Likes:    492
# Dislikes: 0
# Total Accepted:    81.6K
# Total Submissions: 198.6K
# Testcase Example:  '[2,3,2]'
#
# 你是一个专业的小偷，计划偷窃沿街的房屋，每间房内都藏有一定的现金。这个地方所有的房屋都 围成一圈
# ，这意味着第一个房屋和最后一个房屋是紧挨着的。同时，相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警 。
# 
# 给定一个代表每个房屋存放金额的非负整数数组，计算你 在不触动警报装置的情况下 ，能够偷窃到的最高金额。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：nums = [2,3,2]
# 输出：3
# 解释：你不能先偷窃 1 号房屋（金额 = 2），然后偷窃 3 号房屋（金额 = 2）, 因为他们是相邻的。
# 
# 
# 示例 2：
# 
# 
# 输入：nums = [1,2,3,1]
# 输出：4
# 解释：你可以先偷窃 1 号房屋（金额 = 1），然后偷窃 3 号房屋（金额 = 3）。
# 偷窃到的最高金额 = 1 + 3 = 4 。
# 
# 示例 3：
# 
# 
# 输入：nums = [0]
# 输出：0
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
    def rob(self, nums: List[int]) -> int:
        ## 动态规划的解法
        # 因为首尾相连只需考虑三种情况
        # 1、首尾都不包含
        # 2、含首不含尾
        # 3、含尾不含首
        # 在以上3种情况下取最大值即可，而2、3两种情况实际上是包含了1的，所以最终：
        # return max(2, 3)
        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])

        def help(start, end):
            dp_2 = nums[start]
            dp_1 = max(nums[start], nums[start+1])

            for i in range(start+2, end):
                dp_i = max(dp_1, dp_2+nums[i])
                dp_2 = dp_1
                dp_1 = dp_i
            return dp_1

        return max(help(0, n-1), help(1, n))

# @lc code=end

