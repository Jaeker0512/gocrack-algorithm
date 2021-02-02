#
# @lc app=leetcode.cn id=904 lang=python3
#
# [904] 水果成篮
#
# https://leetcode-cn.com/problems/fruit-into-baskets/description/
#
# algorithms
# Medium (42.89%)
# Likes:    65
# Dislikes: 0
# Total Accepted:    10.1K
# Total Submissions: 23.5K
# Testcase Example:  '[1,2,1]'
#
# 在一排树中，第 i 棵树产生 tree[i] 型的水果。
# 你可以从你选择的任何树开始，然后重复执行以下步骤：
# 
# 
# 把这棵树上的水果放进你的篮子里。如果你做不到，就停下来。
# 移动到当前树右侧的下一棵树。如果右边没有树，就停下来。
# 
# 
# 请注意，在选择一颗树后，你没有任何选择：你必须执行步骤 1，然后执行步骤 2，然后返回步骤 1，然后执行步骤 2，依此类推，直至停止。
# 
# 你有两个篮子，每个篮子可以携带任何数量的水果，但你希望每个篮子只携带一种类型的水果。
# 
# 用这个程序你能收集的水果树的最大总量是多少？
# 
# 
# 
# 示例 1：
# 
# 输入：[1,2,1]
# 输出：3
# 解释：我们可以收集 [1,2,1]。
# 
# 
# 示例 2：
# 
# 输入：[0,1,2,2]
# 输出：3
# 解释：我们可以收集 [1,2,2]
# 如果我们从第一棵树开始，我们将只能收集到 [0, 1]。
# 
# 
# 示例 3：
# 
# 输入：[1,2,3,2,2]
# 输出：4
# 解释：我们可以收集 [2,3,2,2]
# 如果我们从第一棵树开始，我们将只能收集到 [1, 2]。
# 
# 
# 示例 4：
# 
# 输入：[3,3,3,1,2,1,1,2,3,3,4]
# 输出：5
# 解释：我们可以收集 [1,2,1,1,2]
# 如果我们从第一棵树或第八棵树开始，我们将只能收集到 4 棵水果树。
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= tree.length <= 40000
# 0 <= tree[i] < tree.length
# 
# 
#

# @lc code=start
class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        left, right = 0, 0
        from collections import defaultdict
        window = defaultdict(int)
        valid = 0
        max_num = 0
        cur_num = 0

        while right < len(tree):
            right_tree = tree[right]
            if window[right_tree] == 0:
                valid += 1
            window[right_tree] += 1
            cur_num += 1
            right += 1

            while valid > 2:
                left_tree = tree[left]
                left += 1
                window[left_tree] -= 1
                cur_num -= 1
                if window[left_tree] == 0:
                    valid -= 1
                if valid <= 2:
                    max_num = max(cur_num, max_num)
            max_num = max(cur_num, max_num)
        return max_num
# @lc code=end

