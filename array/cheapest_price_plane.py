class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:

        self.maps = defaultdict(list)
        self.costs = {}
        self.memo = {}
        for i in range(len(flights)):
            start, end, cost = flights[i]
            self.maps[start].append(end)
            self.costs[(start, end)] = cost

        def dfs(start, end, k):
            if start == end:
                return 0
            if k < 0:
                return math.inf
            if (start, k) in self.memo:
                return self.memo[(start, k)]
            res = math.inf
            for i in self.maps[start]:
                res = min(res, dfs(i, end, k-1) + self.costs[(start, i)])
            self.memo[(start, k)] = res
            return res

        result = dfs(src, dst, K)
        print(self.maps)
        print(self.costs)
        return result if result != math.inf else -1
