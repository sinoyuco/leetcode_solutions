class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        maps = {}
        return self.rec_call(m,n,maps)
        
    def rec_call(self, m, n, maps):
        if m == 1 or n == 1:
            return 1
        if (m,n-1) not in maps:
            maps[(m,n-1)] = self.rec_call(m, n-1, maps)
        if (m-1,n) not in maps:
            maps[(m-1,n)] = self.rec_call(m-1, n, maps)
        return maps[(m, n-1)] + maps[(m-1, n)]
        