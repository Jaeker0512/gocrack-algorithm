#
# @lc app=leetcode.cn id=992 lang=python3
#
# [992] K 个不同整数的子数组
#
# https://leetcode-cn.com/problems/subarrays-with-k-different-integers/description/
#
# algorithms
# Hard (32.81%)
# Likes:    143
# Dislikes: 0
# Total Accepted:    6.3K
# Total Submissions: 19.1K
# Testcase Example:  '[1,2,1,2,3]\n2'
#
# 给定一个正整数数组 A，如果 A 的某个子数组中不同整数的个数恰好为 K，则称 A 的这个连续、不一定独立的子数组为好子数组。
# 
# （例如，[1,2,3,1,2] 中有 3 个不同的整数：1，2，以及 3。）
# 
# 返回 A 中好子数组的数目。
# 
# 
# 
# 示例 1：
# 
# 输入：A = [1,2,1,2,3], K = 2
# 输出：7
# 解释：恰好由 2 个不同整数组成的子数组：[1,2], [2,1], [1,2], [2,3], [1,2,1], [2,1,2],
# [1,2,1,2].
# 
# 
# 示例 2：
# 
# 输入：A = [1,2,1,3,4], K = 3
# 输出：3
# 解释：恰好由 3 个不同整数组成的子数组：[1,2,1,3], [2,1,3], [1,3,4].
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= A.length <= 20000
# 1 <= A[i] <= A.length
# 1 <= K <= A.length
# 
# 
#

# @lc code=start
class Solution:
    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:
        return self.atmost(A, K) - self.atmost(A, K-1)
        
    def atmost(self, A, K):
        left, right = 0, 0
        from collections import defaultdict
        window = defaultdict(int)
        valid = 0
        res = 0
        while right < len(A):
            num = A[right]
            if window[num] == 0:
                valid += 1
            window[num] += 1
            right += 1

            while valid > K:
                left_num = A[left]
                left += 1
                window[left_num] -= 1
                if window[left_num] < 1:
                    valid -= 1
            res += right - left + 1
        return res




        
# @lc code=end

