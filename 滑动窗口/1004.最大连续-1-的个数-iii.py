#
# @lc app=leetcode.cn id=1004 lang=python3
#
# [1004] 最大连续1的个数 III
#
# https://leetcode-cn.com/problems/max-consecutive-ones-iii/description/
#
# algorithms
# Medium (55.87%)
# Likes:    143
# Dislikes: 0
# Total Accepted:    20.6K
# Total Submissions: 36.7K
# Testcase Example:  '[1,1,1,0,0,0,1,1,1,1,0]\n2'
#
# 给定一个由若干 0 和 1 组成的数组 A，我们最多可以将 K 个值从 0 变成 1 。
# 
# 返回仅包含 1 的最长（连续）子数组的长度。
# 
# 
# 
# 示例 1：
# 
# 输入：A = [1,1,1,0,0,0,1,1,1,1,0], K = 2
# 输出：6
# 解释： 
# [1,1,1,0,0,1,1,1,1,1,1]
# 粗体数字从 0 翻转到 1，最长的子数组长度为 6。
# 
# 示例 2：
# 
# 输入：A = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], K = 3
# 输出：10
# 解释：
# [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
# 粗体数字从 0 翻转到 1，最长的子数组长度为 10。
# 
# 
# 
# 提示：
# 
# 
# 1 <= A.length <= 20000
# 0 <= K <= A.length
# A[i] 为 0 或 1 
# 
# 
#

# @lc code=start
class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        l, r = 0, 0
        max_len = 0
        limit = 0

        while r < len(A):
            r_val = A[r]
            if r_val == 0:
                limit += 1
            r += 1

            while limit > K:
                l_val = A[l]
                if l_val == 0:
                    limit -= 1
                l += 1
            max_len = max(max_len, r - l)
        return max_len


        
# @lc code=end

