import collections
class Solution:
    def judgeCircle(self, moves: str) -> bool:
        maps = collections.Counter(moves)
        return maps['L'] == maps['R'] and maps['D'] == maps['U']
