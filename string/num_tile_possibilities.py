class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        count = 0

        def dfs(tiles):
            uniq = set(tiles)
            for i in uniq:
                nonlocal count
                count += 1
                t = [k for k in tiles]
                t.remove(i)
                dfs(t)

        dfs(tiles)
        return count
