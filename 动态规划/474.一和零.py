#
# @lc app=leetcode.cn id=474 lang=python3
#
# [474] 一和零
#
# https://leetcode-cn.com/problems/ones-and-zeroes/description/
#
# algorithms
# Medium (55.65%)
# Likes:    359
# Dislikes: 0
# Total Accepted:    33.8K
# Total Submissions: 60.8K
# Testcase Example:  '["10","0001","111001","1","0"]\n5\n3'
#
# 给你一个二进制字符串数组 strs 和两个整数 m 和 n 。
# 
# 
# 请你找出并返回 strs 的最大子集的大小，该子集中 最多 有 m 个 0 和 n 个 1 。
# 
# 如果 x 的所有元素也是 y 的元素，集合 x 是集合 y 的 子集 。
# 
# 
# 
# 
# 示例 1：
# 
# 
# 输入：strs = ["10", "0001", "111001", "1", "0"], m = 5, n = 3
# 输出：4
# 解释：最多有 5 个 0 和 3 个 1 的最大子集是 {"10","0001","1","0"} ，因此答案是 4 。
# 其他满足题意但较小的子集包括 {"0001","1"} 和 {"10","1","0"} 。{"111001"} 不满足题意，因为它含 4 个 1 ，大于
# n 的值 3 。
# 
# 
# 示例 2：
# 
# 
# 输入：strs = ["10", "0", "1"], m = 1, n = 1
# 输出：2
# 解释：最大的子集是 {"0", "1"} ，所以答案是 2 。
# 
# 
# 
# 
# 提示：
# 
# 
# 1 
# 1 
# strs[i] 仅由 '0' 和 '1' 组成
# 1 
# 
# 
#

# @lc code=start
from numpy.lib.arraysetops import intersect1d


class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        ## dp table 解法1
        # m ----> 0
        # n ----> 1
        # s = len(strs)
        # dp = [[[0] * (n + 1) for i in range(m + 1 )] for i in range(s + 1)]
        # dict_help = {}
        # for idx, string in enumerate(strs):
        #     dict_help[(0, idx)] = string.count('0')
        #     dict_help[(1, idx)] = string.count('1')
        

        # for i in range(1, s+1):
        #     cnt_0 = dict_help[(0, i-1)]
        #     cnt_1 = dict_help[(1, i-1)]
        #     for j in range(m+1):
        #         for k in range(n+1):
        #             # dp[i-1][j][k]代表不放入当前的元素
        #             if j-cnt_0 < 0 or k-cnt_1 < 0:
        #                 dp[i][j][k] = dp[i-1][j][k]
        #             else:
        #                 dp[i][j][k] = max(dp[i-1][j][k],
        #                             dp[i-1][j-cnt_0][k-cnt_1] + 1
        #                             )
        # return int(dp[s][m][n])

        ## dp table 解法2
        # m ----> 0
        # n ----> 1
        # 需要降维
        s = len(strs)
        dp = [[0] * (n + 1) for i in range(m + 1 )]
        dict_help = {}
        for idx, string in enumerate(strs):
            dict_help[(0, idx)] = string.count('0')
            dict_help[(1, idx)] = string.count('1')
    
        for i in range(1, s+1):
            cnt_0 = dict_help[(0, i-1)]
            cnt_1 = dict_help[(1, i-1)]
            for j in range(m, -1, -1):
                for k in range(n, -1, -1):
                    # dp[i-1][j][k]代表不放入当前的元素
                    if j-cnt_0 < 0 or k-cnt_1 < 0:
                        continue
                    else:
                        dp[j][k] = max(dp[j][k],
                                    dp[j-cnt_0][k-cnt_1] + 1
                                    )
        return dp[m][n]
# @lc code=end

