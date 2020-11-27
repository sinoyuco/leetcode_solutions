class Solution:
    def countSubstrings(self, s: str) -> int:
        n, res = len(s), 0
        for i in range(n):
            j = 0
            while i-j >= 0 and i+j < n and s[i-j] == s[i+j]:
                j += 1
                res += 1
            j = 0
            while i-j >= 0 and i+j+1 < n and s[i-j] == s[i+j+1]:
                j += 1
                res += 1
        return res
