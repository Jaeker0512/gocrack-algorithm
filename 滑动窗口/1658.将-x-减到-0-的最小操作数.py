#
# @lc app=leetcode.cn id=1658 lang=python3
#
# [1658] 将 x 减到 0 的最小操作数
#
# https://leetcode-cn.com/problems/minimum-operations-to-reduce-x-to-zero/description/
#
# algorithms
# Medium (26.80%)
# Likes:    45
# Dislikes: 0
# Total Accepted:    4.7K
# Total Submissions: 17.4K
# Testcase Example:  '[1,1,4,2,3]\n5'
#
# 给你一个整数数组 nums 和一个整数 x 。每一次操作时，你应当移除数组 nums 最左边或最右边的元素，然后从 x 中减去该元素的值。请注意，需要
# 修改 数组以供接下来的操作使用。
# 
# 如果可以将 x 恰好 减到 0 ，返回 最小操作数 ；否则，返回 -1 。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：nums = [1,1,4,2,3], x = 5
# 输出：2
# 解释：最佳解决方案是移除后两个元素，将 x 减到 0 。
# 
# 
# 示例 2：
# 
# 
# 输入：nums = [5,6,7,8,9], x = 4
# 输出：-1
# 
# 
# 示例 3：
# 
# 
# 输入：nums = [3,2,20,1,1,3], x = 10
# 输出：5
# 解释：最佳解决方案是移除后三个元素和前两个元素（总共 5 次操作），将 x 减到 0 。
# 
# 
# 
# 
# 提示：
# 
# 
# 1 
# 1 
# 1 
# 
# 
#

# @lc code=start
class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        nums_sum = sum(nums)
        target = nums_sum - x
        if nums_sum < x:
            return -1
        max_len = 0
        l, r = 0, 0

        while r < len(nums):
            num = nums[r]
            r += 1
            target -= num

            while target < 0:
                l_num = nums[l]
                l += 1
                target += l_num
            if target == 0:
                max_len = max(max_len, r - l)
        if max_len == 0 and nums_sum != x:
            return -1 
        return len(nums) - max_len
                
# @lc code=end

