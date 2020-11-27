import collections
class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        maps = collections.Counter(s)
        for i in range(len(s)):
            if maps[s[i]] < k:
                j = i+1
                while j < len(s) - 1 and maps[s[j]] < k:
                    j += 1
                return max(self.longestSubstring(s[:i], k), self.longestSubstring(s[j:], k))
        return len(s)
