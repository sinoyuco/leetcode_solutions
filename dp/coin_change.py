import math

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [math.inf]*(amount+1)
        dp[0] = 0

        for c in coins:
            for j in range(c, amount+1):
                dp[j] = min(dp[j], dp[j-c]+1)
                print(dp)
        return dp[-1] if dp[-1] != math.inf else -1
