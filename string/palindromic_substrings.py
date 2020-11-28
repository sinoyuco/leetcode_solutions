class Solution:
    def countSubstrings(self, s: str) -> int:
        n, res = len(s), 0
        for i in range(n):
            # for each character, expand around, checking the leading and preceding characters at reach iteration.
            j = 0
            # odd
            while i-j >= 0 and i+j < n and s[i-j] == s[i+j]:
                j += 1
                res += 1
            k = 0
            # even
            while i-k >= 0 and i+k+1 < n and s[i-k] == s[i+k+1]:
                k += 1
                res += 1
        return res
