class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def dfs(s, path, res):
            if not s:
                res.append(path[:])
                return
            for i in range(1, len(s)+1):
                if s[:i] != s[i-1::-1]:
                    continue
                dfs(s[i:], path[:]+[s[:i]], res)

        dfs(s, [], res)
        return res
