#
# @lc app=leetcode.cn id=46 lang=python3
#
# [46] 全排列
#
# https://leetcode-cn.com/problems/permutations/description/
#
# algorithms
# Medium (77.53%)
# Likes:    1142
# Dislikes: 0
# Total Accepted:    257.1K
# Total Submissions: 331.2K
# Testcase Example:  '[1,2,3]'
#
# 给定一个 没有重复 数字的序列，返回其所有可能的全排列。
# 
# 示例:
# 
# 输入: [1,2,3]
# 输出:
# [
# ⁠ [1,2,3],
# ⁠ [1,3,2],
# ⁠ [2,1,3],
# ⁠ [2,3,1],
# ⁠ [3,1,2],
# ⁠ [3,2,1]
# ]
# 
#

# @lc code=start
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        track = []
        res = []
        def backtrack(nums, track):
            if len(track) == len(nums):
                res.append(track.copy())
                return
            
            for i in range(len(nums)):
                if nums[i] in track:
                    continue
                track.append(nums[i])
                backtrack(nums, track)
                track.pop()
        backtrack(nums, track)
        return res


    


# @lc code=end

