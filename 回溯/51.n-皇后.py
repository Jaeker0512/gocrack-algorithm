#
# @lc app=leetcode.cn id=51 lang=python3
#
# [51] N 皇后
#
# https://leetcode-cn.com/problems/n-queens/description/
#
# algorithms
# Hard (73.61%)
# Likes:    753
# Dislikes: 0
# Total Accepted:    103.8K
# Total Submissions: 140.9K
# Testcase Example:  '4'
#
# n 皇后问题 研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。
# 
# 给你一个整数 n ，返回所有不同的 n 皇后问题 的解决方案。
# 
# 
# 
# 每一种解法包含一个不同的 n 皇后问题 的棋子放置方案，该方案中 'Q' 和 '.' 分别代表了皇后和空位。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：n = 4
# 输出：[[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
# 解释：如上图所示，4 皇后问题存在两个不同的解法。
# 
# 
# 示例 2：
# 
# 
# 输入：n = 1
# 输出：[["Q"]]
# 
# 
# 
# 
# 提示：
# 
# 
# 1 
# 皇后彼此不能相互攻击，也就是说：任何两个皇后都不能处于同一条横行、纵行或斜线上。
# 
# 
# 
# 
#

# @lc code=start
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        board = [["." for _ in range(n)] for _ in range(n)]

        def is_valid(board, row, col):
            # 判断同列是否有冲突
            for i in range(row):
                if board[i][col] == 'Q':
                    return False
            # 判断左上是否有冲突
            for i, j in zip(range(row-1, -1, -1), range(col-1, -1, -1)):
                if board[i][j] == 'Q':
                    return False
            # 判断右上是否有冲突
            for i, j in zip(range(row-1, -1, -1), range(col+1, n)):
                if board[i][j] == 'Q':
                    return False
            return True

        def backtrack(board, row):
            if row == len(board):
                res.append(["".join(board[i]) for i in range(n)])

            for col in range(n):
                if not is_valid(board, row, col):
                    continue
                board[row][col] = 'Q'
                backtrack(board, row+1)
                board[row][col] = '.'

        backtrack(board, 0)
        return res




# @lc code=end

