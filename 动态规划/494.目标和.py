#
# @lc app=leetcode.cn id=494 lang=python3
#
# [494] 目标和
#
# https://leetcode-cn.com/problems/target-sum/description/
#
# algorithms
# Medium (44.89%)
# Likes:    590
# Dislikes: 0
# Total Accepted:    69.4K
# Total Submissions: 154.6K
# Testcase Example:  '[1,1,1,1,1]\n3'
#
# 给定一个非负整数数组，a1, a2, ..., an, 和一个目标数，S。现在你有两个符号 + 和 -。对于数组中的任意一个整数，你都可以从 + 或
# -中选择一个符号添加在前面。
# 
# 返回可以使最终数组和为目标数 S 的所有添加符号的方法数。
# 
# 
# 
# 示例：
# 
# 输入：nums: [1, 1, 1, 1, 1], S: 3
# 输出：5
# 解释：
# 
# -1+1+1+1+1 = 3
# +1-1+1+1+1 = 3
# +1+1-1+1+1 = 3
# +1+1+1-1+1 = 3
# +1+1+1+1-1 = 3
# 
# 一共有5种方法让最终目标和为3。
# 
# 
# 
# 
# 提示：
# 
# 
# 数组非空，且长度不会超过 20 。
# 初始的数组的和不会超过 1000 。
# 保证返回的最终结果能被 32 位整数存下。
# 
# 
#

# @lc code=start
class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        n = len(nums)
        ## 递归 备忘录 解法
        # memo = dict()
        # def dp(cur_sum, idx):
        #     if (cur_sum, idx) in memo:
        #         return memo[(cur_sum, idx)]
        #     if idx > n-1:
        #         if cur_sum == S:
        #             return 1
        #         return 0
        #     # 因为现在要求的是有几种解法，那自然备忘录和递归返回都是解法数量
        #     ret1 = dp(cur_sum + nums[idx], idx+1)
        #     ret2 = dp(cur_sum + -1*nums[idx], idx+1)
        #     memo[(cur_sum, idx)] = ret1 + ret2
        #     return memo[(cur_sum, idx)]
        # return dp(0, 0)
        
        ## dp table 解法1
        # 如何转化为01背包问题呢。
        # 假设加法的总和为x，那么减法对应的总和就是sum - x。
        # 所以我们要求的是 x - (sum - x) = S
        # x = (S + sum) / 2
        # 此时问题就转化为，装满容量为x背包，有几种方法。
        # sum_nums = sum(nums)
        # if (sum_nums + S) & 1 != 0 or sum_nums < S:
        #     return 0
        # target = int((sum_nums + S)/2)
        # dp = [[0 for _ in range(target+1)] for _ in range(2)]

        # for i in range(2):
        #     dp[i][0] = 1

        # for i in range(1, n+1):
        #     for j in range(0, target+1):
        #         if j-nums[i-1] < 0:
        #             dp[1][j] = dp[0][j]
        #         else:
        #             dp[1][j]  = dp[0][j] + dp[0][j-nums[i-1]]
        #     dp[0] = dp[1].copy()
        # return dp[1][target]

        ## dp table 解法2
        # 如何转化为01背包问题呢。
        # 假设加法的总和为x，那么减法对应的总和就是sum - x。
        # 所以我们要求的是 x - (sum - x) = S
        # x = (S + sum) / 2
        # 此时问题就转化为，装满容量为x背包，有几种方法。
        # 降维成一维
        sum_nums = sum(nums)
        if (sum_nums + S) & 1 != 0 or sum_nums < S:
            return 0
        target = int((sum_nums + S)/2)
        dp = [0 for _ in range(target+1)]
        dp[0] = 1

        for i in range(1, n+1):
            for j in range(target, -1, -1):
                if j-nums[i-1] < 0:
                    continue
                else:
                    dp[j]  = dp[j] + dp[j-nums[i-1]]
        return dp[target]
# @lc code=end

