class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        if len(strs) == 0:
            return ''
        if len(strs) == 1:
            return strs[0]

        l = math.inf
        for i in strs:
            l = min(l, len(i))

        i = 0
        while i < l:
            f = strs[0][i]

            for s in range(1, len(strs)):
                if f != strs[s][i]:
                    return strs[s][:i]

            i += 1
        return strs[0][:i] if i > 0 else ''
