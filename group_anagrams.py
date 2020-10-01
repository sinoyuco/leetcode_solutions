class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # O (n*m where m is the length of the strings)
        maps = {}
        for i in strs:
            l = ''.join([k for k in sorted(list(i))])
            if l in maps:
                maps[l].append(i)
            else:
                maps[l] = [i]
        return maps.values()


