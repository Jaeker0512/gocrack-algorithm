#
# @lc app=leetcode.cn id=15 lang=python3
#
# [15] 三数之和
#
# https://leetcode-cn.com/problems/3sum/description/
#
# algorithms
# Medium (30.75%)
# Likes:    2951
# Dislikes: 0
# Total Accepted:    416.1K
# Total Submissions: 1.3M
# Testcase Example:  '[-1,0,1,2,-1,-4]'
#
# 给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有和为 0
# 且不重复的三元组。
# 
# 注意：答案中不可以包含重复的三元组。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：nums = [-1,0,1,2,-1,-4]
# 输出：[[-1,-1,2],[-1,0,1]]
# 
# 
# 示例 2：
# 
# 
# 输入：nums = []
# 输出：[]
# 
# 
# 示例 3：
# 
# 
# 输入：nums = [0]
# 输出：[]
# 
# 
# 
# 
# 提示：
# 
# 
# 0 
# -10^5 
# 
# 
#

# @lc code=start
from typing import TypeVar


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        def two_sum(nums, target):
            size = len(nums)
            left, right = 0, size-1
            res = []
            while left < right:
                tmp = nums[left] + nums[right]
                left_val, right_val = nums[left], nums[right]
                if tmp < target:
                    while left < right and nums[left]==left_val:
                        left += 1
                elif tmp > target:
                    while left < right and nums[right]==right_val:
                        right-=1
                else:
                    res.append([left_val, right_val])
                    while left < right and nums[left]==left_val:
                        left += 1
                    while left < right and nums[right]==right_val:
                        right-=1
            return res
        threesum_res = []
        size = len(nums)
        i = 0
        while i < size:
            twosum_res = two_sum(nums[i+1:], 0 - nums[i])
            for ls in twosum_res:
                ls.append(nums[i])
                threesum_res.append(ls)
            while i < size-1 and nums[i] == nums[i+1]:
                i += 1
            i += 1

        
        return threesum_res
                    
# @lc code=end

