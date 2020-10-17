class Solution:
    def changeTwo(self, amount: int, coins: List[int]) -> int:

        # [1],[1],[2],[2],[3],[4],
        #  0   1   2   3   4   5

        dp = [0]*(amount+1)
        dp[0] = 1

        for c in coins:
            for t in range(c, amount+1):
                dp[t] += dp[t-c]
        return dp[-1]
