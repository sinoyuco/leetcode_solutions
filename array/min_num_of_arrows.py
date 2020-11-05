import math
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        p = sorted(points)
        count = 0
        current = [-math.inf]*2

        for i in range(len(p)):
            if p[i][0] > current[1]:
                current = p[i]
                count += 1
            else:
                current[1] = min(current[1], p[i][1])
        return count
