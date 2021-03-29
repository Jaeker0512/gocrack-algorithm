#
# @lc app=leetcode.cn id=887 lang=python3
#
# [887] 鸡蛋掉落
#
# https://leetcode-cn.com/problems/super-egg-drop/description/
#
# algorithms
# Hard (28.94%)
# Likes:    595
# Dislikes: 0
# Total Accepted:    40.3K
# Total Submissions: 139.3K
# Testcase Example:  '1\n2'
#
# 给你 k 枚相同的鸡蛋，并可以使用一栋从第 1 层到第 n 层共有 n 层楼的建筑。
# 
# 已知存在楼层 f ，满足 0  ，任何从 高于 f 的楼层落下的鸡蛋都会碎，从 f 楼层或比它低的楼层落下的鸡蛋都不会破。
# 
# 每次操作，你可以取一枚没有碎的鸡蛋并把它从任一楼层 x 扔下（满足 1
# ）。如果鸡蛋碎了，你就不能再次使用它。如果某枚鸡蛋扔下后没有摔碎，则可以在之后的操作中 重复使用 这枚鸡蛋。
# 
# 请你计算并返回要确定 f 确切的值 的 最小操作次数 是多少？
# 
# 
# 示例 1：
# 
# 
# 输入：k = 1, n = 2
# 输出：2
# 解释：
# 鸡蛋从 1 楼掉落。如果它碎了，肯定能得出 f = 0 。 
# 否则，鸡蛋从 2 楼掉落。如果它碎了，肯定能得出 f = 1 。 
# 如果它没碎，那么肯定能得出 f = 2 。 
# 因此，在最坏的情况下我们需要移动 2 次以确定 f 是多少。 
# 
# 
# 示例 2：
# 
# 
# 输入：k = 2, n = 6
# 输出：3
# 
# 
# 示例 3：
# 
# 
# 输入：k = 3, n = 14
# 输出：4
# 
# 
# 
# 
# 提示：
# 
# 
# 1 
# 1 
# 
# 
#

# @lc code=start
class Solution:
    def superEggDrop(self, k: int, n: int) -> int:
        # 还是先尝试递归备忘录的方法吧 居然超时
        # memo = dict()
        # def dp(n, k):
        #     # 定义base case
        #     if (n,k) in memo:
        #         return memo[(n,k)]
        #     if n == 0:
        #         return 0
        #     if k == 1:
        #         return n

        #     res = float('INF')
        #     ## 最坏情况下求最小值才是至少的含义
        #     # 别被这个至少给混淆了
        #     lo, hi = 1, n
        #     mid = (lo + hi)//2
        #     while lo <= hi:
        #         mid = (lo + hi)//2
        #         broken = dp(mid-1, k-1)
        #         not_broken = dp(n-mid, k)
        #         if broken > not_broken:
        #             hi = mid - 1
        #             res = min(res, broken+1)
        #         else:
        #             lo = mid + 1
        #             res = min(res, not_broken+1)
        #     # for i in range(1, n+1): # 我得做选择呀，每层楼都得扔扔看
        #     #     res = min(res, max(
        #     #         dp(n-i, k), # 没碎
        #     #         dp(i-1, k-1) # 碎了
        #     #         ) + 1 # 在第 i 楼扔了一次
        #     #         )
        #     memo[(n, k)] = res
        #     return res
        # return dp(n, k)

        ## dp table 解法 居然也超时卧槽
        # dp = [[9999 for _ in range(k+1)] for _ in range(n+1)]

        # ## 初始化base case
        # for j in range(k+1):
        #     dp[0][j] = 0
        #     if j > 0:
        #         dp[1][j] = 1 # 楼层为1， 1 个以及 1 个鸡蛋以上只需要扔 1 次

        # for i in range(n+1):
        #     dp[i][0] = 0 # 鸡蛋个数为0，不管楼层多少都测不出
        #     dp[i][1] = i # 鸡蛋个数为1，不管楼层多少都需要线性扫描

        # for i in range(2, n+1):
        #     for j in range(2, k+1):
        #         lo, hi = 1, i
        #         while lo <= hi:
        #             mid = (lo + hi)//2
        #             broken = dp[mid-1][j-1]
        #             not_broken = dp[i-mid][j]

        #             if broken > not_broken:
        #                 hi = mid - 1
        #                 dp[i][j] = min(dp[i][j], broken+1)
        #             else:
        #                 lo = mid + 1
        #                 dp[i][j] = min(dp[i][j], not_broken+1)
        #         # dp[i][j] = max(dp[lo-1][j-1], dp[i-lo][j]) + 1
        # return dp[n][k]

        ## 解法3
        # 将问题从： N 个楼层，有 K 个蛋，求最少要扔 T 次，才能保证当 F 无论是 0 <= F <= N 中哪个值，都能测试出来
        # 转变为：有 K 个蛋，扔 T 次，求可以确定 F 的个数，然后得出 N 个楼层

        dp = [[0 for _ in range(n+1)] for _ in range(k+1)]

        m = 0
        while dp[k][m] < n:
            m += 1
            for i in range(1, k+1):
                dp[i][m] = dp[i-1][m-1] + dp[i][m-1] + 1
        return m



# @lc code=end

