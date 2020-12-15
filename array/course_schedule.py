import collections
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        maps = collections.defaultdict(set)
        countmap = [0] * numCourses
        st = []
        count = 0

        for i in prerequisites:
            maps[i[1]].add(i[0])
            countmap[i[0]] += 1

        for i in range(numCourses):
            if countmap[i] == 0:
                st.append(i)

        while st:
            curr = st.pop()
            for i in maps[curr]:
                countmap[i] -= 1
                if countmap[i] == 0:
                    st.append(i)
            count += 1

        return count == numCourses
