#
# @lc app=leetcode.cn id=153 lang=python3
#
# [153] 寻找旋转排序数组中的最小值
#
# https://leetcode-cn.com/problems/find-minimum-in-rotated-sorted-array/description/
#
# algorithms
# Medium (52.26%)
# Likes:    343
# Dislikes: 0
# Total Accepted:    101.5K
# Total Submissions: 194.2K
# Testcase Example:  '[3,4,5,1,2]'
#
# 假设按照升序排序的数组在预先未知的某个点上进行了旋转。例如，数组 [0,1,2,4,5,6,7]  可能变为 [4,5,6,7,0,1,2] 。
# 
# 请找出其中最小的元素。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：nums = [3,4,5,1,2]
# 输出：1
# 
# 
# 示例 2：
# 
# 
# 输入：nums = [4,5,6,7,0,1,2]
# 输出：0
# 
# 
# 示例 3：
# 
# 
# 输入：nums = [1]
# 输出：1
# 
# 
# 
# 
# 提示：
# 
# 
# 1 
# -5000 
# nums 中的所有整数都是 唯一 的
# nums 原来是一个升序排序的数组，但在预先未知的某个点上进行了旋转
# 
# 
#

# @lc code=start
class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            if nums[l] < nums[r]:
                return nums[l]
            mid = l + (r- l)//2
            if nums[l] <= nums[mid]:
                l = mid + 1
            elif nums[l] > nums[mid]:
                r = mid

        return nums[l-1]
# 可参考 https://leetcode-cn.com/problems/find-minimum-in-rotated-sorted-array/solution/yi-wen-jie-jue-4-dao-sou-suo-xuan-zhuan-pai-xu-s-3/
# @lc code=end

