class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key=lambda x: x[0])
        res = [intervals[0]]
        for i in range(1, len(intervals)):
            curr = intervals[i]
            if curr[0] <= res[-1][1]:
                if curr[1] >= res[-1][1]:
                    res[-1][1] = curr[1]
            else:
                res.append(curr)
        return res
