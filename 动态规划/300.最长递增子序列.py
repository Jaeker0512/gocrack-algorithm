#
# @lc app=leetcode.cn id=300 lang=python3
#
# [300] 最长递增子序列
#
# https://leetcode-cn.com/problems/longest-increasing-subsequence/description/
#
# algorithms
# Medium (48.23%)
# Likes:    1473
# Dislikes: 0
# Total Accepted:    234K
# Total Submissions: 482.7K
# Testcase Example:  '[10,9,2,5,3,7,101,18]'
#
# 给你一个整数数组 nums ，找到其中最长严格递增子序列的长度。
# 
# 子序列是由数组派生而来的序列，删除（或不删除）数组中的元素而不改变其余元素的顺序。例如，[3,6,2,7] 是数组 [0,3,1,6,2,2,7]
# 的子序列。
# 
# 
# 示例 1：
# 
# 
# 输入：nums = [10,9,2,5,3,7,101,18]
# 输出：4
# 解释：最长递增子序列是 [2,3,7,101]，因此长度为 4 。
# 
# 
# 示例 2：
# 
# 
# 输入：nums = [0,1,0,3,2,3]
# 输出：4
# 
# 
# 示例 3：
# 
# 
# 输入：nums = [7,7,7,7,7,7,7]
# 输出：1
# 
# 
# 
# 
# 提示：
# 
# 
# 1 
# -10^4 
# 
# 
# 
# 
# 进阶：
# 
# 
# 你可以设计时间复杂度为 O(n^2) 的解决方案吗？
# 你能将算法的时间复杂度降低到 O(n log(n)) 吗?
# 
# 
#

# @lc code=start
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        ## 先自己尝试用dp来解决
        n = len(nums)
        ## 如果数组nums不是空的，那至少递增子序列长度是1
        # 先明确一下dp数组的含义dp[i]代表前i+1个元素当中子序列的长度
        # 注意！！！dp[i]的定义
        # 输出：不能返回最后一个状态值，最后一个状态值只表示以 nums[len - 1] 
        # 结尾的「上升子序列」的长度，状态数组 dp 的最大值才是题目要求的结果
        # dp = [1 for _ in range(n)]

        # for i in range(1, n):
        #     for j in range(i):
        #         if nums[j] < nums[i]:
        #             dp[i] = max(dp[i], dp[j]+1)
        # return max(dp)

        ## 尝试用贪心加上二分法来解决
        # 二分找到第一个比target大的数的下标
        def help(arr, target):
            left, right = 0, len(arr)-1

            while left <= right:
                mid = left + (right - left)//2
                if arr[mid] < target:
                    left = mid + 1
                elif arr[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
            return left

        tail = []
        if n > 0:
            tail.append(nums[0])
        for i in range(1, n):
            num = nums[i]
            if num > tail[-1]:
                tail.append(num)
            elif num < tail[-1]:
                k = help(tail, num)
                if tail[k-1] == num:
                    continue
                tail[k] = num
        return len(tail)




# @lc code=end

