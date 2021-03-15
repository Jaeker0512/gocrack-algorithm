#
# @lc app=leetcode.cn id=64 lang=python3
#
# [64] 最小路径和
#
# https://leetcode-cn.com/problems/minimum-path-sum/description/
#
# algorithms
# Medium (68.23%)
# Likes:    815
# Dislikes: 0
# Total Accepted:    189.4K
# Total Submissions: 277.6K
# Testcase Example:  '[[1,3,1],[1,5,1],[4,2,1]]'
#
# 给定一个包含非负整数的 m x n 网格 grid ，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。
# 
# 说明：每次只能向下或者向右移动一步。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：grid = [[1,3,1],[1,5,1],[4,2,1]]
# 输出：7
# 解释：因为路径 1→3→1→1→1 的总和最小。
# 
# 
# 示例 2：
# 
# 
# 输入：grid = [[1,2,3],[4,5,6]]
# 输出：12
# 
# 
# 
# 
# 提示：
# 
# 
# m == grid.length
# n == grid[i].length
# 1 
# 0 
# 
# 
#

# @lc code=start
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        ## 递归备忘录 解法
        # memo = dict()
        # max_value = float("INF")
        # def dp(i, j):
        #     if (i, j) in memo and memo[(i, j)] != max_value:
        #         return memo[(i, j)]
        #     if i < 0 or j < 0:
        #         return max_value
        #     if i == 0 and j == 0:
        #         return grid[i][j]
        #     memo[(i, j)] = min(dp(i - 1, j), dp(i, j - 1)) + grid[i][j]
        #     return memo[(i, j)]
        # return dp(m-1, n-1)

        ## dp table 解法
        dp = [[float("INF") for _ in range(n)] for _ in range(m)]
        dp[0][0] = grid[0][0]
        for i in range(1, m):
            dp[i][0] = dp[i-1][0] + grid[i][0]
        for j in range(1, n):
            dp[0][j] = dp[0][j-1] + grid[0][j]
        
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
        return dp[m-1][n-1]

# @lc code=end

