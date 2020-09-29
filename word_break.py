def wordBreak(self, s: str, wordDict: List[str]) -> bool:
    maps = {}
    #    for i in wordDict:
    #         maps[i] = 1

    #     j = 1
    #     while j <= len(s):
    #         if s in maps:
    #             return True

    #         if s[0:j] in maps:
    #             s = s[j:]
    #             j = 1
    #         else:
    #             j += 1

    #     return True if s == '' else False
    for j in wordDict:
            if len(j) in dic:
                maps[len(j)].append(j)
            else:
                maps[len(j)]=[j]
        
        dp=[1]+[0]*len(s)
        for i in range(len(s)):
            for k in dic:
                if i-k+1>=0 and dp[i-k+1] and s[i-k+1:i+1] in dic[k]:
                    dp[i+1]=1
        print(dp)
        return dp[-1]
