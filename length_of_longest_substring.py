class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maps = {}
        start, max_val = -1, 0
        #abcabcbb
        for i in range(len(s)):
            if s[i] in maps:
                start = max(start, maps[s[i]])
            max_val = max(max_val, i-start)
            maps[s[i]] = i
        return max_val
