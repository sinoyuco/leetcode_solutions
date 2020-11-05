class Solution:
    def helper(self, grid, i, j):
        queue = [(i, j)]
        vis = set()
        while queue:
            c = queue.pop()
            if c not in vis:

                ci, cj = c
                grid[ci][cj] = '#'

                if ci > 0 and grid[ci-1][cj] == '1':
                    queue.append((ci-1, cj))

                if ci < len(grid)-1 and grid[ci+1][cj] == '1':
                    queue.append((ci+1, cj))

                if cj > 0 and grid[ci][cj-1] == '1':
                    queue.append((ci, cj-1))

                if cj < len(grid[0])-1 and grid[ci][cj+1] == '1':
                    queue.append((ci, cj+1))
                vis.add((ci, cj))

    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "1":
                    count += 1
                    self.helper(grid, i, j)
        return count
