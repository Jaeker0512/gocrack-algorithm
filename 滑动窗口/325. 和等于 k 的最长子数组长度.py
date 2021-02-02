class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        distance = 0
        prefix_sum = 0
        sum_map = {0:-1}
        prefix_sum = 0
        for i in range(len(nums)):
            prefix_sum += nums[i]
            if prefix_sum not in sum_map:
                sum_map[prefix_sum] = i
            if prefix_sum - k in sum_map:
                distance = max(distance,  abs(i - sum_map[prefix_sum - k]))

        return distance