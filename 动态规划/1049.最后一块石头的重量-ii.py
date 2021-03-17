#
# @lc app=leetcode.cn id=1049 lang=python3
#
# [1049] 最后一块石头的重量 II
#
# https://leetcode-cn.com/problems/last-stone-weight-ii/description/
#
# algorithms
# Medium (50.93%)
# Likes:    142
# Dislikes: 0
# Total Accepted:    9.2K
# Total Submissions: 17.9K
# Testcase Example:  '[2,7,4,1,8,1]'
#
# 有一堆石头，每块石头的重量都是正整数。
# 
# 每一回合，从中选出任意两块石头，然后将它们一起粉碎。假设石头的重量分别为 x 和 y，且 x <= y。那么粉碎的可能结果如下：
# 
# 
# 如果 x == y，那么两块石头都会被完全粉碎；
# 如果 x != y，那么重量为 x 的石头将会完全粉碎，而重量为 y 的石头新重量为 y-x。
# 
# 
# 最后，最多只会剩下一块石头。返回此石头最小的可能重量。如果没有石头剩下，就返回 0。
# 
# 
# 
# 示例：
# 
# 输入：[2,7,4,1,8,1]
# 输出：1
# 解释：
# 组合 2 和 4，得到 2，所以数组转化为 [2,7,1,8,1]，
# 组合 7 和 8，得到 1，所以数组转化为 [2,1,1,1]，
# 组合 2 和 1，得到 1，所以数组转化为 [1,1,1]，
# 组合 1 和 1，得到 0，所以数组转化为 [1]，这就是最优值。
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= stones.length <= 30
# 1 <= stones[i] <= 1000
# 
# 
#

# @lc code=start
class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        stones_weight = sum(stones)
        bag_cap = stones_weight/2 # 背包的容量
        n = len(stones)
        ## 递归备忘录 解法
        # memo = dict()
        # def dp(cur_weight, idx):
        #     if (cur_weight, idx) in memo:
        #         return memo[(cur_weight, idx)]
        #     if cur_weight >= bag_cap or idx > n-1:
        #         return abs(2*cur_weight - stones_weight)
        #     memo[(cur_weight, idx)] = min(
        #                     dp(cur_weight, idx + 1),
        #                     dp(cur_weight + stones[idx], idx + 1)
        #     )
        #     return memo[(cur_weight, idx)]
        # return dp(0, 0)

        ## dp table 解法
        bag_cap = int(bag_cap)
        dp =[[0 for _ in range(bag_cap+1)] for _ in range(n+1)]

        for i in range(1, n+1):
            for j in range(0, bag_cap+1):
                if j - stones[i-1] < 0:
                    dp[i][j] = dp[i-1][j]
                else:
                    ##而dp[i-1][w-wt[i-1]]也很好理解：
                    # 你如果想装第i个物品，你怎么计算这时候的最大价值？
                    # 换句话说，在装第i个物品的前提下，背包能装的最大价值是多少？
                    # 因为现在已经确定要把第i个物品装进背包，此时背包剩余容量：
                    # j - stones[i-1]，在这个剩余容量的前提下寻求最大价值。
                    dp[i][j] = max(
                            dp[i-1][j],
                            dp[i-1][j-stones[i-1]]+stones[i-1]
                    )
        return stones_weight - 2*dp[n][bag_cap]

            
# @lc code=end

