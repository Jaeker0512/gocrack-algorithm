#
# @lc app=leetcode.cn id=69 lang=python3
#
# [69] x 的平方根
#
# https://leetcode-cn.com/problems/sqrtx/description/
#
# algorithms
# Easy (39.16%)
# Likes:    586
# Dislikes: 0
# Total Accepted:    254K
# Total Submissions: 648.4K
# Testcase Example:  '4'
#
# 实现 int sqrt(int x) 函数。
# 
# 计算并返回 x 的平方根，其中 x 是非负整数。
# 
# 由于返回类型是整数，结果只保留整数的部分，小数部分将被舍去。
# 
# 示例 1:
# 
# 输入: 4
# 输出: 2
# 
# 
# 示例 2:
# 
# 输入: 8
# 输出: 2
# 说明: 8 的平方根是 2.82842..., 
# 由于返回类型是整数，小数部分将被舍去。
# 
# 
#

# @lc code=start
class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 2, int(x/2)
        if x == 0:
            return 0
        elif x == 1:
            return 1

        while l <= r:
            mid = l + (r-l)//2
            if mid**2 > x:
                r = mid - 1
            elif mid**2 < x:
                l = mid + 1
            elif mid**2 ==x:
                return int(mid)
        return int(l-1)

# @lc code=end

