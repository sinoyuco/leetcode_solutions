class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        maps = {}
        for i in range(len(S)):
            if S[i] in maps:
                maps[S[i]].append(i)
            else:
                maps[S[i]] = [i]

        result = []
        c = set()
        for i in range(len(S)):
            if i == maps[S[i]][0]:
                c.add(S[i])
            if i == maps[S[i]][-1]:
                c.remove(S[i])
            if len(c) == 0:
                result.append(i)
        a = []
        for j in range(len(result)):
            if j == 0:
                a.append(len(S[:result[j]])+1)
            else:
                a.append(len(S[result[j-1]:result[j]]))
        return a
