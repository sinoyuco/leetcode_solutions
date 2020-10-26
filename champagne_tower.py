class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        dp = [[0 for i in range(j)] for j in range(1, query_row+2)]
        dp[0][0] = poured
        for i in range(query_row):
            for j in range(len(dp[i])):
                t = (dp[i][j]-1)/2
                if t > 0:
                    dp[i+1][j] += t
                    dp[i+1][j+1] += t

        target = dp[query_row][query_glass]
        return target if target < 1 else 1
