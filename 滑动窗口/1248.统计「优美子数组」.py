#
# @lc app=leetcode.cn id=1248 lang=python3
#
# [1248] 统计「优美子数组」
#
# https://leetcode-cn.com/problems/count-number-of-nice-subarrays/description/
#
# algorithms
# Medium (54.65%)
# Likes:    152
# Dislikes: 0
# Total Accepted:    27.7K
# Total Submissions: 50.7K
# Testcase Example:  '[1,1,2,1,1]\n3'
#
# 给你一个整数数组 nums 和一个整数 k。
# 
# 如果某个 连续 子数组中恰好有 k 个奇数数字，我们就认为这个子数组是「优美子数组」。
# 
# 请返回这个数组中「优美子数组」的数目。
# 
# 
# 
# 示例 1：
# 
# 输入：nums = [1,1,2,1,1], k = 3
# 输出：2
# 解释：包含 3 个奇数的子数组是 [1,1,2,1] 和 [1,2,1,1] 。
# 
# 
# 示例 2：
# 
# 输入：nums = [2,4,6], k = 1
# 输出：0
# 解释：数列中不包含任何奇数，所以不存在优美子数组。
# 
# 
# 示例 3：
# 
# 输入：nums = [2,2,2,1,2,2,1,2,2,2], k = 2
# 输出：16
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= nums.length <= 50000
# 1 <= nums[i] <= 10^5
# 1 <= k <= nums.length
# 
# 
#

# @lc code=start
class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        return self.atmostk(nums, k) - self.atmostk(nums, k-1)
        
        
    def atmostk(self, nums, k):
        l, r = 0, 0
        ans = 0
        while r < len(nums):
            num = nums[r]
            r += 1
            if num % 2 != 0:
                k -= 1

            while k < 0:
                l_num = nums[l]
                l += 1
                if l_num % 2 != 0:
                    k += 1
            
            ans += r - l + 1
        return ans
# @lc code=end

