#
# @lc app=leetcode.cn id=416 lang=python3
#
# [416] 分割等和子集
#
# https://leetcode-cn.com/problems/partition-equal-subset-sum/description/
#
# algorithms
# Medium (49.53%)
# Likes:    697
# Dislikes: 0
# Total Accepted:    107.6K
# Total Submissions: 217.1K
# Testcase Example:  '[1,5,11,5]'
#
# 给定一个只包含正整数的非空数组。是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。
# 
# 注意:
# 
# 
# 每个数组中的元素不会超过 100
# 数组的大小不会超过 200
# 
# 
# 示例 1:
# 
# 输入: [1, 5, 11, 5]
# 
# 输出: true
# 
# 解释: 数组可以分割成 [1, 5, 5] 和 [11].
# 
# 
# 
# 
# 示例 2:
# 
# 输入: [1, 2, 3, 5]
# 
# 输出: false
# 
# 解释: 数组不能分割成两个元素和相等的子集.
# 
# 
# 
# 
#

# @lc code=start
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sum_nums = sum(nums)
        if sum_nums & 1 != 0:
            return False
        target = int(sum_nums/2) # 背包的容量
        n = len(nums)
        ## 递归备忘录 解法
        # memo = dict()
        # def dfs(sum_nums, idx):
        #     if (sum_nums, idx) in memo:
        #         return memo[(sum_nums, idx)]
        #     if sum_nums > target or idx > len(nums)-1:
        #         return False
        #     if sum_nums == target:
        #         return True
        #     memo[(sum_nums, idx)] = dfs(sum_nums + nums[idx], idx+1) or dfs(sum_nums, idx+1)
        #     return memo[(sum_nums, idx)]
        # return dfs(0, 0)

        ## dp table 解法
        ## nums即需要装载的物体，只不过现在这边是需要把包正好装满
        dp = [[False for _ in range(target+1)] for _ in range(n+1)]
        for i in range(n+1):
            dp[i][0] = True
        for i in range(1, n+1):
            for j in range(0, target+1):
                if j - nums[i-1] < 0:
                    ## 背包容量不够啦，别装了
                    dp[i][j] = dp[i - 1][j]
                else:
                    # 这里状态转移方程在于
                    dp[i][j] = dp[i - 1][j] or dp[i-1][j-nums[i-1]]
        return dp[n][target]
# @lc code=end

