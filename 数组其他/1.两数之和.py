#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#
# https://leetcode-cn.com/problems/two-sum/description/
#
# algorithms
# Easy (50.04%)
# Likes:    10249
# Dislikes: 0
# Total Accepted:    1.7M
# Total Submissions: 3.5M
# Testcase Example:  '[2,7,11,15]\n9'
#
# 给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 的那 两个 整数，并返回它们的数组下标。
# 
# 你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。
# 
# 你可以按任意顺序返回答案。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：nums = [2,7,11,15], target = 9
# 输出：[0,1]
# 解释：因为 nums[0] + nums[1] == 9 ，返回 [0, 1] 。
# 
# 
# 示例 2：
# 
# 
# 输入：nums = [3,2,4], target = 6
# 输出：[1,2]
# 
# 
# 示例 3：
# 
# 
# 输入：nums = [3,3], target = 6
# 输出：[0,1]
# 
# 
# 
# 
# 提示：
# 
# 
# 2 
# -10^9 
# -10^9 
# 只会存在一个有效答案
# 
# 
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        help_map = {}
        for i, num in enumerate(nums):
            if target - num in help_map:
                return [help_map[target - num], i]
            if num not in help_map:
                help_map[num] = i
            
# @lc code=end

