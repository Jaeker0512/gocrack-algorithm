#
# @lc app=leetcode.cn id=912 lang=python3
#
# [912] 排序数组
#
# https://leetcode-cn.com/problems/sort-an-array/description/
#
# algorithms
# Medium (59.53%)
# Likes:    286
# Dislikes: 0
# Total Accepted:    148.3K
# Total Submissions: 252.1K
# Testcase Example:  '[5,2,3,1]'
#
# 给你一个整数数组 nums，请你将该数组升序排列。
# 
# 
# 
# 
# 
# 
# 示例 1：
# 
# 输入：nums = [5,2,3,1]
# 输出：[1,2,3,5]
# 
# 
# 示例 2：
# 
# 输入：nums = [5,1,1,2,0,0]
# 输出：[0,0,1,1,2,5]
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= nums.length <= 50000
# -50000 <= nums[i] <= 50000
# 
# 
#

# @lc code=start
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        ## 优化过的快排
        def quicksort(nums, l, r):
            if l >= r:
                return
            pivot = randint(l, r)
            nums[l], nums[pivot] = nums[pivot], nums[l]
            i, j = l, r
            while i < j:
                while i < j  and nums[j] > nums[l]:
                    j -= 1
                while i < j and nums[i] <= nums[l]:
                    i += 1
                nums[i], nums[j] = nums[j], nums[i]
            nums[l], nums[i] = nums[i], nums[l]

            quicksort(nums, l, j-1)
            quicksort(nums, j+1, r)

        ## 归并排序
        def merge(nums, left, mid, right):
            i, j = left, mid + 1
            tmp = []
            while i <= mid or j <= right:
                if (j <= right and nums[i] > nums[j]) or i > mid:
                    tmp.append(nums[j])
                    j += 1
                else:
                    tmp.append(nums[i])
                    i += 1
            nums[left:right+1] = tmp

        def mergesort(nums, left, right):
            if left >= right:
                return
            mid = (left + right)//2
            ## 分
            mergesort(nums, left, mid)
            mergesort(nums, mid+1, right)
            ## 合并
            merge(nums, left, mid, right)


        ## 堆排序
        def HeadAdjust(nums, root, length):
            parent = root  
            while parent * 2 + 1 < length:
                left = parent * 2 + 1
                right = parent * 2 + 2
                if right >= length or nums[left] > nums[right]:
                    child_idx = left
                else:
                    child_idx = right
                if nums[parent] < nums[child_idx]:
                    nums[parent], nums[child_idx] = nums[child_idx], nums[parent]
                    parent = child_idx
                else:
                    break
        length = len(nums)
        ## 建最大堆
        for i in range(length-1, -1, -1):
            HeadAdjust(nums, i, length)
        for j in range(length-1, -1, -1):
            nums[0], nums[j] = nums[j], nums[0]
            HeadAdjust(nums, 0, j)

        # quicksort(nums, 0, len(nums) - 1)
        # mergesort(nums, 0, len(nums) - 1)
        return nums
# @lc code=end

