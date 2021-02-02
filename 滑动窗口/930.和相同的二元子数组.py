#
# @lc app=leetcode.cn id=930 lang=python3
#
# [930] 和相同的二元子数组
#
# https://leetcode-cn.com/problems/binary-subarrays-with-sum/description/
#
# algorithms
# Medium (38.78%)
# Likes:    84
# Dislikes: 0
# Total Accepted:    5.3K
# Total Submissions: 13.7K
# Testcase Example:  '[1,0,1,0,1]\n2'
#
# 在由若干 0 和 1  组成的数组 A 中，有多少个和为 S 的非空子数组。
# 
# 
# 
# 示例：
# 
# 输入：A = [1,0,1,0,1], S = 2
# 输出：4
# 解释：
# 如下面黑体所示，有 4 个满足题目要求的子数组：
# [1,0,1,0,1]
# [1,0,1,0,1]
# [1,0,1,0,1]
# [1,0,1,0,1]
# 
# 
# 
# 
# 提示：
# 
# 
# A.length <= 30000
# 0 <= S <= A.length
# A[i] 为 0 或 1
# 
# 
#

# @lc code=start
class Solution:
    def numSubarraysWithSum(self, A: List[int], S: int) -> int:
        res = 0
        prefix_sum = 0
        from collections import defaultdict
        sum_map = defaultdict(int)
        sum_map[0] = 1
        prefix_sum = 0
        for i in range(len(A)):
            prefix_sum += A[i]
            if prefix_sum - S in sum_map:
                res +=  sum_map[prefix_sum - S]
            sum_map[prefix_sum] += 1
        return res
# @lc code=end

