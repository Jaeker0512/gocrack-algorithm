#
# @lc app=leetcode.cn id=77 lang=python3
#
# [77] 组合
#
# https://leetcode-cn.com/problems/combinations/description/
#
# algorithms
# Medium (76.35%)
# Likes:    499
# Dislikes: 0
# Total Accepted:    134.4K
# Total Submissions: 175.7K
# Testcase Example:  '4\n2'
#
# 给定两个整数 n 和 k，返回 1 ... n 中所有可能的 k 个数的组合。
# 
# 示例:
# 
# 输入: n = 4, k = 2
# 输出:
# [
# ⁠ [2,4],
# ⁠ [3,4],
# ⁠ [2,3],
# ⁠ [1,2],
# ⁠ [1,3],
# ⁠ [1,4],
# ]
# 
#

# @lc code=start
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        track = []
        res = []
        
        def backtrack(start, track):
            if len(track) == k:
                res.append(track.copy()) 
            for i in range(start, n+1):
                if k-len(track) > n-i+1:
                    break
                track.append(i)
                backtrack(i+1, track)
                track.pop()
        backtrack(1, track)
        return res
# @lc code=end

