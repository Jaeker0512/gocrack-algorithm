#
# @lc app=leetcode.cn id=354 lang=python3
#
# [354] 俄罗斯套娃信封问题
#
# https://leetcode-cn.com/problems/russian-doll-envelopes/description/
#
# algorithms
# Hard (43.22%)
# Likes:    485
# Dislikes: 0
# Total Accepted:    52.5K
# Total Submissions: 121.2K
# Testcase Example:  '[[5,4],[6,4],[6,7],[2,3]]'
#
# 给你一个二维整数数组 envelopes ，其中 envelopes[i] = [wi, hi] ，表示第 i 个信封的宽度和高度。
# 
# 当另一个信封的宽度和高度都比这个信封大的时候，这个信封就可以放进另一个信封里，如同俄罗斯套娃一样。
# 
# 请计算 最多能有多少个 信封能组成一组“俄罗斯套娃”信封（即可以把一个信封放到另一个信封里面）。
# 
# 注意：不允许旋转信封。
# 
# 
# 示例 1：
# 
# 
# 输入：envelopes = [[5,4],[6,4],[6,7],[2,3]]
# 输出：3
# 解释：最多信封的个数为 3, 组合为: [2,3] => [5,4] => [6,7]。
# 
# 示例 2：
# 
# 
# 输入：envelopes = [[1,1],[1,1],[1,1]]
# 输出：1
# 
# 
# 
# 
# 提示：
# 
# 
# 1 
# envelopes[i].length == 2
# 1 i, hi 
# 
# 
#

# @lc code=start
class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
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
        def lengthOfLIS(nums):
            n = len(nums)
            tail = []
            if n > 0:
                tail.append(nums[0][1])
            for i in range(1, n):
                num = nums[i][1]
                if num > tail[-1]:
                    tail.append(num)
                elif num < tail[-1]:
                    k = help(tail, num)
                    if tail[k-1] == num:
                        continue
                    tail[k] = num
            return len(tail)
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        return lengthOfLIS(envelopes)
# @lc code=end

