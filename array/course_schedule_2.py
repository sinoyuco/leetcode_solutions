import collections


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        maps = collections.defaultdict(set)
        countmap = collections.defaultdict(int)
        stack = []
        count = 0

        for i in prerequisites:
            maps[i[1]].add(i[0])
            countmap[i[0]] += 1

        for i in range(numCourses):
            if countmap[i] == 0:
                stack.append(i)

        res = stack[:]
        while stack:
            curr = stack.pop()
            for i in maps[curr]:
                countmap[i] -= 1
                if countmap[i] == 0:
                    stack.append(i)
                    res.append(i)
            count += 1
        return res if count == numCourses else []
