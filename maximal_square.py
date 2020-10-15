class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        height, width = len(matrix), len(matrix[0])
        dp = [[0]*width for i in range(height)]
        result = 0

        for i in range(height):
            for j in range(width):
                if matrix[i][j] == '1':
                    dp[i][j] = 1
                    if i > 0 and j > 0:
                        dp[i][j] += min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
                    result = max(result, dp[i][j])
        return result*result
