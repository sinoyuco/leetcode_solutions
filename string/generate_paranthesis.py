class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def dfs(v, l, r):
            print(v, l, r)
            if len(v) == (2*n):
                result.append(v)
                return
            if l < n:
                dfs(v+'(', l+1, r)
            if r < l:
                dfs(v+')', l, r+1)
        dfs('', 0, 0)
        return result
