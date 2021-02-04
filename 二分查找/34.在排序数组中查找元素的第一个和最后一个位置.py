#
# @lc app=leetcode.cn id=34 lang=python3
#
# [34] 在排序数组中查找元素的第一个和最后一个位置
#
# https://leetcode-cn.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/
#
# algorithms
# Medium (42.18%)
# Likes:    838
# Dislikes: 0
# Total Accepted:    205.4K
# Total Submissions: 486.8K
# Testcase Example:  '[5,7,7,8,8,10]\n8'
#
# 给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。
# 
# 如果数组中不存在目标值 target，返回 [-1, -1]。
# 
# 进阶：
# 
# 
# 你可以设计并实现时间复杂度为 O(log n) 的算法解决此问题吗？
# 
# 
# 
# 
# 示例 1：
# 
# 
# 输入：nums = [5,7,7,8,8,10], target = 8
# 输出：[3,4]
# 
# 示例 2：
# 
# 
# 输入：nums = [5,7,7,8,8,10], target = 6
# 输出：[-1,-1]
# 
# 示例 3：
# 
# 
# 输入：nums = [], target = 0
# 输出：[-1,-1]
# 
# 
# 
# 提示：
# 
# 
# 0 
# -10^9 
# nums 是一个非递减数组
# -10^9 
# 
# 
#

# @lc code=start
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        return [self.left_bound(nums, target), self.right_bound(nums, target)]
        
    def left_bound(self, nums, target):
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left  + (right - left)//2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            elif nums[mid] == target:
                right = mid - 1
        if left >= len(nums) or nums[left] != target:
            return - 1
        return left
    
    def right_bound(self, nums, target):
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left  + (right - left)//2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            elif nums[mid] == target:
                left = mid + 1
        if right < 0 or nums[right] != target:
            return - 1
        return right
# @lc code=end

