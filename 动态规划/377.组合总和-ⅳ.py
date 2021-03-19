#
# @lc app=leetcode.cn id=377 lang=python3
#
# [377] 组合总和 Ⅳ
#
# https://leetcode-cn.com/problems/combination-sum-iv/description/
#
# algorithms
# Medium (44.03%)
# Likes:    292
# Dislikes: 0
# Total Accepted:    24.4K
# Total Submissions: 55.5K
# Testcase Example:  '[1,2,3]\n4'
#
# 给你一个由 不同 整数组成的数组 nums ，和一个目标整数 target 。请你从 nums 中找出并返回总和为 target
# 的元素组合的个数。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：nums = [1,2,3], target = 4
# 输出：7
# 解释：
# 所有可能的组合为：
# (1, 1, 1, 1)
# (1, 1, 2)
# (1, 2, 1)
# (1, 3)
# (2, 1, 1)
# (2, 2)
# (3, 1)
# 请注意，顺序不同的序列被视作不同的组合。
# 
# 
# 示例 2：
# 
# 
# 输入：nums = [9], target = 3
# 输出：0
# 
# 
# 
# 
# 提示：
# 
# 
# 1 
# 1 
# nums 中的所有元素 互不相同
# 1 
# 
# 
# 
# 
# 进阶：如果给定的数组中含有负数会发生什么？问题会产生何种变化？如果允许负数出现，需要向题目中添加哪些限制条件？
# 
#

# @lc code=start
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        ## 直接上dp的解法，直接一维
        # 如果求组合数就是外层for循环遍历物品，内层for遍历背包。
        # 如果求排列数就是外层for遍历背包，内层for循环遍历物品。
        n = len(nums)
        dp = [0 for _ in range(target+1)]
        dp[0] = 1
        for j in range(1, target + 1):
            for num in nums:
                if j < num:
                    continue
                dp[j] = dp[j] + dp[j-num]

        return dp[target]

        
# @lc code=end

