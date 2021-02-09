#
# @lc app=leetcode.cn id=18 lang=python3
#
# [18] 四数之和
#
# https://leetcode-cn.com/problems/4sum/description/
#
# algorithms
# Medium (39.77%)
# Likes:    739
# Dislikes: 0
# Total Accepted:    152.4K
# Total Submissions: 382.9K
# Testcase Example:  '[1,0,-1,0,-2,2]\n0'
#
# 给定一个包含 n 个整数的数组 nums 和一个目标值 target，判断 nums 中是否存在四个元素 a，b，c 和 d ，使得 a + b + c
# + d 的值与 target 相等？找出所有满足条件且不重复的四元组。
# 
# 注意：
# 
# 答案中不可以包含重复的四元组。
# 
# 示例：
# 
# 给定数组 nums = [1, 0, -1, 0, -2, 2]，和 target = 0。
# 
# 满足要求的四元组集合为：
# [
# ⁠ [-1,  0, 0, 1],
# ⁠ [-2, -1, 1, 2],
# ⁠ [-2,  0, 0, 2]
# ]
# 
# 
#

# @lc code=start
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        def threeSum(nums, target):
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
                twosum_res = two_sum(nums[i+1:], target - nums[i])
                for ls in twosum_res:
                    ls.append(nums[i])
                    threesum_res.append(ls)
                while i < size-1 and nums[i] == nums[i+1]:
                    i += 1
                i += 1
            return threesum_res

        four_res = []
        size = len(nums)
        i = 0
        while i < size:
            threesum_res = threeSum(nums[i+1:], target - nums[i])
            for ls in threesum_res:
                ls.append(nums[i])
                four_res.append(ls)
            while i < size-1 and nums[i] == nums[i+1]:
                i += 1
            i += 1
        return four_res
# @lc code=end

