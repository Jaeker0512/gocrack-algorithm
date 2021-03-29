class Solution:
    def maxA(self, N: int) -> int:
        dp = [0 for _ in range(N+1)]

        for i in range(1, N+1):
            dp[i] = dp[i-1] + 1

            for j in range(2, i):
                dp[i] = max(dp[i], dp[j-2]*(i-j+1))

        return dp[N]