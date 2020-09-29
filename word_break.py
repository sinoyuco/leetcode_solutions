def wordBreak(self, s: str, wordDict: List[str]) -> bool:
      maps = {}
       for i in wordDict:
            maps[i] = 1

        j = 1
        while j <= len(s):
            if s in maps:
                return True

            if s[0:j] in maps:
                s = s[j:]
                j = 1
            else:
                j += 1

        return True if s == '' else False
