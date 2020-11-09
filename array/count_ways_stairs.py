class Solution:
    def count(self, n):
        memo = [-1]*(n+1)
        return self.countWays(n, memo)

    def countWays(self, n, memo):
        if n < 0:
            return 0
        elif n==0:
            return 1
        elif memo[n] > -1:
            return memo[n]
        else:
            memo[n] = self.countWays(n-1, memo) + self.countWays(n-2, memo) + self.countWays(n-3, memo)
            return memo[n]
