class Solution:
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
        m, k = str(n), len(str(n))
        dp = [0]*(k+1)
        dp[-1] = 1
        for i in range(k-1, -1, -1):
            for dig in digits:
                if dig < m[i]:
                    dp[i] += len(digits) ** (k-i-1)
                elif dig == m[i]:
                    dp[i] += dp[i+1]
        return dp[0] + sum(len(digits)**i for i in range(1,k))