class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        self.result = 0

        def dfs(s, seen):
            if not s:
                self.result = max(self.result, len(seen))
            else:
                for i in range(1, len(s)+1):
                    sub = s[:i]
                    if sub not in seen:
                        dfs(s[i:], seen + [sub])

        dfs(s, [])
        return self.result
