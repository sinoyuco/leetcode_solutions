class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        n, m = len(matrix), len(matrix[0])
        seen = set()
        res = []
        i, j = 0, -1
        curr = 1
        div = 0
        dir = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        while curr <= n*m:
            curri, currj = i+dir[div % 4][0], j+dir[div % 4][1]
            if 0 <= curri < n and 0 <= currj < m and (curri, currj) not in seen:
                res.append(matrix[curri][currj])
                i += dir[div % 4][0]
                j += dir[div % 4][1]
                curr += 1
                seen.add((curri, currj))
            else:
                div += 1
        return res
