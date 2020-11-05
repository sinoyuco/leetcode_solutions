class Solution:
    def maxSizeSlices(self, slices: List[int]) -> int:
        if len(slices) == 0:
            return 0

        t = len(slices)//3

        dp = [[0]*len(slices) for i in range(t+1)]
        dp2 = [[0]*len(slices) for i in range(t+1)]

        for i in range(1, t+1):
            for j in range(1, len(slices)):
                if j == 1:
                    dp[i][j] = slices[j-1]
                    dp2[i][j] = slices[j]
                    continue
                dp[i][j] = max(dp[i-1][j-2]+slices[j-1], dp[i][j-1])
                dp2[i][j] = max(dp2[i-1][j-2]+slices[j], dp2[i][j-1])
        return max(dp[-1][-1], dp2[-1][-1])
