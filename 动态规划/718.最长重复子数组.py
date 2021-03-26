#
# @lc app=leetcode.cn id=718 lang=python3
#
# [718] 最长重复子数组
#
# https://leetcode-cn.com/problems/maximum-length-of-repeated-subarray/description/
#
# algorithms
# Medium (55.10%)
# Likes:    402
# Dislikes: 0
# Total Accepted:    54.7K
# Total Submissions: 99K
# Testcase Example:  '[1,2,3,2,1]\n[3,2,1,4,7]'
#
# 给两个整数数组 A 和 B ，返回两个数组中公共的、长度最长的子数组的长度。
# 
# 
# 
# 示例：
# 
# 输入：
# A: [1,2,3,2,1]
# B: [3,2,1,4,7]
# 输出：3
# 解释：
# 长度最长的公共子数组是 [3, 2, 1] 。
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= len(A), len(B) <= 1000
# 0 <= A[i], B[i] < 100
# 
# 
#

# @lc code=start
class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:
        # 直接用动态规划来干就得了
        # 还是先定义dp数组的含义
        # dp[i][j]代表的是以A[i]和B[i]为末尾项的最长公共子数组长度
        # 如果它们俩一样，以它们俩为末尾项的公共子数组，长度保底为1——dp[i][j]至少为 1，
        # 要考虑它们俩的前缀数组——dp[i-1][j-1]能为它们俩提供多大的公共长度
        res = 0
        a, b = len(A), len(B)
        dp = [[0 for _ in range(b+1)] for _ in range(a+1)]
        for i in range(1, a+1):
            for j in range(1, b+1):
                if A[i-1] == B[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                if dp[i][j] > res:
                    res = dp[i][j]
        return res
        ## 可优化空间的
# @lc code=end

