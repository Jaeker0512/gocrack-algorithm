#
# @lc app=leetcode.cn id=90 lang=python3
#
# [90] 子集 II
#
# https://leetcode-cn.com/problems/subsets-ii/description/
#
# algorithms
# Medium (61.77%)
# Likes:    386
# Dislikes: 0
# Total Accepted:    66.6K
# Total Submissions: 107.8K
# Testcase Example:  '[1,2,2]'
#
# 给定一个可能包含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。
# 
# 说明：解集不能包含重复的子集。
# 
# 示例:
# 
# 输入: [1,2,2]
# 输出:
# [
# ⁠ [2],
# ⁠ [1],
# ⁠ [1,2,2],
# ⁠ [2,2],
# ⁠ [1,2],
# ⁠ []
# ]
# 
#

# @lc code=start
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        track = []
        res = []
        def backtrack(nums, start, track):
            res.append(track.copy()) 
            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i-1]:
                    continue
                track.append(nums[i])
                backtrack(nums, i+1, track)
                track.pop()
        backtrack(sorted(nums), 0, track)
        return res
# @lc code=end

