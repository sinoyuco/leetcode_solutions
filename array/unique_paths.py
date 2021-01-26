class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        maps = {}
        return self.rec_call(m,n,maps)

        # dp = [[0 for i in range(n)] for j in range(m)]
        # dp[0][0] = 1
        # for i in range(m):
        #     for j in range(n):
        #         if i == 0 and j > 0:
        #             dp[i][j] = 1
        #         elif i > 0 and j == 0:
        #             dp[i][j] = 1
        #         elif i>0 and j>0:
        #             dp[i][j] += dp[i][j-1] + dp[i-1][j]
        # return dp[-1][-1]
        
    def rec_call(self, m, n, maps):
        if m == 1 or n == 1:
            return 1
        if (m,n-1) not in maps:
            maps[(m,n-1)] = self.rec_call(m, n-1, maps)
        if (m-1,n) not in maps:
            maps[(m-1,n)] = self.rec_call(m-1, n, maps)
        return maps[(m, n-1)] + maps[(m-1, n)]
        