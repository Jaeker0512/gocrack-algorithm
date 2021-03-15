#
# @lc app=leetcode.cn id=96 lang=python3
#
# [96] 不同的二叉搜索树
#
# https://leetcode-cn.com/problems/unique-binary-search-trees/description/
#
# algorithms
# Medium (69.34%)
# Likes:    1052
# Dislikes: 0
# Total Accepted:    109.5K
# Total Submissions: 157.9K
# Testcase Example:  '3'
#
# 给定一个整数 n，求以 1 ... n 为节点组成的二叉搜索树有多少种？
# 
# 示例:
# 
# 输入: 3
# 输出: 5
# 解释:
# 给定 n = 3, 一共有 5 种不同结构的二叉搜索树:
# 
# ⁠  1         3     3      2      1
# ⁠   \       /     /      / \      \
# ⁠    3     2     1      1   3      2
# ⁠   /     /       \                 \
# ⁠  2     1         2                 3
# 
#

# @lc code=start
class Solution:
    def numTrees(self, n: int) -> int:
        ## 递归备忘录 解法
        # memo = dict()
        # def dp(n):
        #     if n in memo:
        #         return memo[n]
        #     if n <= 1:
        #         return 1
        #     count = 0
        #     for i in range(1, n+1):
        #         count += dp(n-i)*dp(i-1)
        #     memo[n] = count
        #     return count
        # return dp(n)
        ## dp table 解法
        dp = [1 for _ in range(n+1)]
        for i in range(2, n+1):
            count = 0
            for j in range(1, i+1):
                count += dp[i - j] * dp[j - 1]
            dp[i] = count
        return dp[n]



# @lc code=end

