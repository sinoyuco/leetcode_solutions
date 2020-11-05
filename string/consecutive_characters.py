class Solution:
    def maxPower(self, s: str) -> int:

        counter = max_val = i = 0
        tracked = ''

        while i < len(s):
            if s[i] == tracked:
                counter += 1
            else:
                tracked = s[i]
                counter = 1
            max_val = max(counter, max_val)
            i += 1
        return max_val
